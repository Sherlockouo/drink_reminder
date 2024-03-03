from flask import Blueprint, request, Response, stream_with_context, jsonify

from service.gpt import chat_with_gpt, chat_with_gpt_stream, get_models


gpt = Blueprint("index", __name__)


@gpt.route("/", methods=["GET"])
def index():
    return "Server is running! ^_^"


@gpt.route("/models", methods=["GET"])
def models():
    model_list = get_models()
    model_data = model_list.data
    # 将model_data转换为字典，以便jsonify可以处理
    models_dict = {"models": [{"id": model.id} for model in model_data]}
    return jsonify(models_dict)


@gpt.route("/chat", methods=["POST"])
def chat():
    msg = request.get_json().get("message")
    model = request.get_json().get("model")
    temperature = request.get_json().get("temperature")

    if (
        msg == ""
        or msg == None
        or (temperature != None and (temperature < 0 or temperature > 1))
    ):
        # nothing happens
        return Response.status_code(400)
    if not model or model == "":
        model = "moonshot-v1-8k"
    if not temperature:
        temperature = 0.3

    print(msg, model, temperature)

    res = chat_with_gpt_stream(
        [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg},
        ],
        model,
        temperature,
    )

    @stream_with_context
    def generate():
        # 迭代流式事件
        for event in res:
            # 提取事件中的文本
            event_text = event.choices[0].delta.content
            if event_text == None:
                break
            # 将文本添加到响应内容中
            yield event_text

    return Response(stream_with_context(generate()), mimetype="text/event-stream")
