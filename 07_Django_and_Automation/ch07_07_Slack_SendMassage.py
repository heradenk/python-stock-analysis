import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2368539513475-2365329030277-SX5xuhmj0ixPNq0BybG6VUEN"
 
post_message(myToken,"#일반","https://upload3.inven.co.kr/upload/2021/08/14/bbs/i16548237894.jpg")
#10열 토큰, 12열 (2)채널 (3)메시지만 바꿔주면 
