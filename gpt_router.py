import json
from flask import Blueprint,request,Response,stream_with_context

from gpt import chat_with_gpt, chat_with_gpt_stream
from sendmsg import send_msg
from drink_reminder import msgs

gpt = Blueprint('index', __name__)

@gpt.route('/', methods=['GET','POST'])
def index():
    # print("request ",)
    if request.form.get('type') != 'text':
        # nothing happens
        send_msg(messageSender,"听不懂你在说什么哦！")
        return 
    source = request.form.get('source')
    sourceJson = json.loads(source)
    messageSender = sourceJson['from']['payload']['name']
    
    message = request.form.get('content')
    
    res = chat_with_gpt(message,model="gpt-4")
    replyMsg = res.choices[0].message.content
    send_msg(messageSender,replyMsg)
    return "OK"

@gpt.route('/chat', methods=['GET','POST'])
def chat():
    
    msg = request.get_json().get("message")
    
    if msg == "" or  msg == None :
        # nothing happens
        return Response()
    
    res = chat_with_gpt_stream(msg,model="moonshot-v1-8k")
        
    @stream_with_context()
    def generate():
        # 迭代流式事件
        for event in res:
            # 提取事件中的文本
            event_text = event.choices[0].delta.content
            if event_text == None:
                break
            # 将文本添加到响应内容中
            yield event_text

    return Response(stream_with_context(generate()), mimetype='text/event-stream')


