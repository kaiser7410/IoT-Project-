#中華電信物聯網大平台 串接服務模組
import requests #Http Client
import json
#定義Global全域變數
chtHost='https://iot.cht.com.tw/iot/v1'
#專案金鑰(readonly)
readKey='PKTPT4SA9BRARZ27U7'
#專案可讀寫資料key
rwKey='PKT7GHAC1UMZ11TF1P'
deviceID='36817231809'


#定義功能 串接特定SesorID 讀取最後一筆資料下來
def readLastData(sensorID):
    #例外管理(Outside 不可控)
    try:
        #定義取得感測器資料網址
        urlString=f'{chtHost}/device/{deviceID}/sensor/{sensorID}/rawdata'
        #採用dict設定Headers
        myHeaders={'CK':readKey}
        #使用前端Http Client採用GET方式提出請求
        response=requests.get(url=urlString,headers=myHeaders) #一個請求一個回應物件
        #讀回資料json
        jsonData=response.json() #dict物件
        return jsonData #沒有決定Http status 預設為200
    except Exception as ex:
        raise Exception("網路不通了") #拋出例外物件 重新建構配置訊息

#模組要進行感測器字串資料寫入(CHT IOT平台)
def sensorTextDataWrite(sensorid,sensorData):
    #服務位址
    addURL=f'{chtHost}/device/{deviceID}/rawdata'
    #設定Http Header 使用dict
    myHeader={"CK":rwKey,"Content-Type":"application/json"}
    #準備傳送上去的資料
    sourceData=[{"id":sensorid,"save":True,"value":[sensorData]}]
    print(sourceData)
    #採用Http Client 採用Request Method-POST
    response=requests.post(url=addURL,data=json.dumps(sourceData),headers=myHeader)
    #判斷回應Http status code
    if response.status_code==200:
        #新增成功
        return "新增成功"
    else:
        return "新增失敗"
