#引用模組建構的Flask物件
from webmodules import app
#引用flask模組代理前端的request物件
from flask import request
#引用Request Client
import requests
from webmodules.DbUtility import connectionOpen,insert,update,queryForObject
from webmodules.LineModules import sendReplyTextMessage,sendReplyFriendMessage

#定義常數
lineToken='t7SKfVopcUJ5SRAHRwxOR9jAFRtNG2uzZDllG5nGtQELs83M0tAsrMOTGC7m1l1gZaw8DAsSPk61PaghzG4uDoZM9vXsmWv/ufCyyfed5gSNbi2Vg/u8UvCpRVXyo/RmUyFFNKdw+6mnoIXCveQVAgdB04t89/1O/w1cDnyilFU='
#定義掛勾Line Bot服務
@app.route("/api/v1/webhook/service",methods=['POST'])
def webhookProcess():
    response=None

    json=request.get_json()
    #取通用屬性user id replytoken
    data=json['events'][0]
   
    source=data['source']
    userid=None
    #判斷是否為個人使用者
    if source['type']=='user':
        userid=source['userId']

      
    #判斷訊息是哪一種事件type(follow/message/unfollow..)
    if data['type']=='follow':
        replytoken=data['replyToken'] #unfollow封鎖 沒有這一個屬性
        print(f'userid:{userid} replytoken:{replytoken}')  
        #取出必要的屬性 (user id/replytoken/getprofile...displayname..image)
        #呼喚getprofile api
        urlString='https://api.line.me/v2/bot/profile/'+userid
        #準備Http request GET header Authorization:Bearer <token>
        myHeaders={"Authorization":"Bearer "+lineToken}
        response=requests.get(urlString,headers=myHeaders)
        print(response.json())
        profile=response.json()
        #取出稱呼與相片資訊
        name=profile['displayName']
        photo=profile['pictureUrl']
        #進行現有資料查詢 如果有 那就是解鎖 如果沒有 就是新增
        connection=connectionOpen()
        #呼叫查詢function
        result=queryForObject(connection,"select UserId,Name from LineUser where UserId=%s",(userid))
        print(result)
        if result==None:
            
            #新增
            #儲存到資料庫資料表去 userid name phtoto(或者資料表解鎖)
            update(connection,"Insert Into LineUser(UserId,Name,PictureURL) values(%s,%s,%s)",(userid,name,photo))
        else:
            #解鎖更新記錄
            update(connection,'Update LineUser Set Active=1 Where UserID=%s',(userid))
            message='歡迎你回到家...'
            sendReplyFriendMessage(lineToken,replytoken,message)
        
        
        return ""
    elif data['type']=='unfollow':
        #封鎖 修改現有資料active 
        connection=connectionOpen()
        update(connection,'Update LineUser Set Active=0 Where UserID=%s',(userid))
        print('被封鎖了')
        #無須回應訊息到使用者
        return ""
    elif data['type']=='message':
        replytoken=data['replyToken'] 
        #聊天訊息 文字(自然語言應用NLP I進行分析)
        msgObj=data['message']
        #判斷聊天內容是文字
        if msgObj["type"]=="text":
            #取出聊天內容
            content=msgObj["text"]
            #TODO 串接NLP(or chatgpt) Service進行語言解析
            #已讀已回(鸚鵡)
            sendReplyTextMessage(lineToken,replytoken,content)
        pass
