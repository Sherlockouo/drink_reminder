import json
from flask import Blueprint,request

from gpt import chat_with_gpt
from sendmsg import send_msg

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
