import schedule
from datetime import datetime
import json 
import requests
import time
import random


msgs = ["喝水时间到啦！一杯清新的水正在向你招手呢！不要让你的身体感到口渴，保持水分是我们身体的基本需求哦！",
        "您已经有一段时间没有喝水了，记得补充水分哦！",
        "不要忘记喝水，保持良好的水分平衡对身体健康非常重要。",
        "休息一下，喝口水，让自己的身体和大脑得到放松。",
        "喝水可以帮助你清醒，提高工作效率，现在就去喝一杯吧！",
"早晨的第一缕阳光，搭配一杯清新的水，唤醒沉睡的身体，新的一天，从喝水开始！🌞💧",
"工作间隙，别忘了给身体补充水分，一杯水，让思绪更清晰，效率加倍！💼🍵",
"运动后大汗淋漓？及时补充水分，让身体恢复活力，喝水也能很时尚哦！🏃‍♀️💦            ",
"下午茶时间，一杯柠檬水，清新又解渴，美丽肌肤喝出来！🍋🍵                               ",
"读书时，一杯温开水陪伴，让知识与水分一起滋养心灵。📚💧                                 ",
"出门在外，随身携带水杯，随时补充水分，健康生活，从小事做起。🚶‍♂️🥤                ",
"睡前一杯水，缓解一天的疲劳，让身体在夜间也能好好休息。🌙💤                             ",
"喝水也能很浪漫，和爱人共享一杯水，甜蜜满分！❤️🥂                                        ",
"忙碌的你，记得喝水哦！水分是美丽的秘密武器，让你容光焕发。💃💧                         ",
"喝水，不仅是为了解渴，更是为了健康。每天八杯水，健康生活不打烊！🏋️‍♀️💪            ",
"早晨起床，一杯温水开启新的一天，让身体慢慢苏醒，迎接挑战！🌅🥛                         ",
"喝水，是最简单的养生之道。一杯水，一份健康，一份好心情。🌼💧                           ",
"喝水，就像给生活添加一抹清新，让每一天都充满活力。🌟💧                                 ",
"喝水，是对自己最好的呵护。记得，身体需要水分，就像心灵需要爱。💖💧                     ",
"喝水，让身体像花儿一样绽放。每天保持水分，美丽自然来。🌹💦                             ",
"喝水，是最简单的美容秘诀。一杯水，让肌肤喝饱水，焕发自然光彩。💧🌺                     ",
"喝水，是生活的一种态度。简单，却能带来不简单的改变。🌿💧                               ",
"喝水，让生活更有节奏。工作再忙，也要记得给自己补充水分。🎶💧                           ",
"喝水，是健康的开始。每天一杯水，让身体更强壮，生活更美好。🏋️‍♂️💪                  "
        ]
print("starting...\n")                                                          

def send_reminder():
    url = 'http://127.0.0.1:3010/webhook/msg/v2'
    headers = {'Content-Type': 'application/json'}
    msg = random.choice(msgs)  # 随机选择一条消息

    data = [{
        "to": {"alias":"611"},
        "data": {"content":msg} 
    },{
        "to": "origin",
        "data": {"content":msg} 
        }
            ]

    response = requests.post(url, headers=headers, data=json.dumps(data))
     
    if response.status_code == 200:
        print('提醒发送成功')
    else:
        print(f'提醒发送失败, 状态码: {response.status_code}, 响应内容: {response.text}')

# 从8点到22点，每个小时的第0分钟发送提醒
for i in range(8, 22):
    schedule.every().day.at(f"{i:02d}:00").do(send_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)

