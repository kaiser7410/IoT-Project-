#Line API串接服務模組設計
import requests #HttpClient
import json
#常數架構
replyMessageURL='https://api.line.me/v2/bot/message/reply'

#回復訊息到使用者端(借助ReplyToken)
def sendReplyTextMessage(lineToken,replyToken,message):
    Ltoken="Bearer "+lineToken
    #建構Header(dict物件)
    myHeaders={"Authorization":Ltoken,"Content-Type":"application/json"}
    message=[{"type":"text","text":message}]
    try:
        #回送資料
        data={"replyToken":replyToken,"messages":message}
        requests.post(replyMessageURL,data=json.dumps(data),headers=myHeaders)
    except Exception as ex:
        raise ex 

#回復訊息到使用者端(借助ReplyToken)
def sendReplyFriendMessage(lineToken,replyToken,message):
    Ltoken="Bearer "+lineToken
    #建構Header(dict物件)
    myHeaders={"Authorization":Ltoken,"Content-Type":"application/json"}
    message=[{"type":"text","text":message},{"type":"sticker","packageId":"1070","stickerId":"17841"}]
    try:
        #回送資料
        data={"replyToken":replyToken,"messages":message}
        requests.post(replyMessageURL,data=json.dumps(data),headers=myHeaders)
    except Exception as ex:
        raise ex          
