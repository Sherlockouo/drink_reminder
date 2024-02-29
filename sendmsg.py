import json
import requests

def send_msg(msgReceiver,msg):
    # url = 'http://127.0.0.1:3010/webhook/msg/v2'
    url = 'http://192.168.10.32:3010/webhook/msg/v2'
    headers = {'Content-Type': 'application/json'}

    data = [{
        "to": msgReceiver,
        "data": {"content":msg} 
    }
            ]

    response = requests.post(url, headers=headers, data=json.dumps(data))
     
    if response.status_code == 200:
        print('提醒发送成功')
    else:
        print(f'提醒发送失败, 状态码: {response.status_code}, 响应内容: {response.text}')