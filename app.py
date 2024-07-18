#設計網站系統初始化 與啟動網站系統
from webmodules import app
from flask import Flask,render_template,request #引用Flask類別 產生個體物件 進行網站初始化設定
from webmodules.CHTIotService import readLastData,sensorTextDataWrite
#定義一個Global Variable全域變數 參照一個Flask物件
import json
from datetime import datetime


# app.config.update(CONFIGS)
#定義首頁端點入口 http://localhost:5566/ or /home
#畫地圖 描述端點end point 
#@xxx decorator 裝飾(實現語法糖重新描述)
@app.route("/")
@app.route("/home")
def home():
    #直接回應資料
    return "<font size='6' color='red'>Hello World</font>"

#打招呼端點 調用頁面
@app.route("/hello")
def hello():
    #產生狀態
    company='華梵大學' #str字串物件 company local variable(區域變數)
    #使用render_template() function 回應字串 就會交給jinja2 template引擎 去調用頁面
    #透過Request生命週期 持續若干狀態
    return render_template('helloworld.html',message=company)

#調用頁面 採用WebSocket Client訂閱CHT IOT WebSocket Server-推播環境人體入侵監測空間
@app.route('/show/pir')
def showPIR():
    return render_template('showpir.html')


#提供一個匝道服務 傳遞感測器id進來 串接 CHT Iot智慧聯網找出相對感測器最後一筆資料
#前端要採用QueryString http://hosted/iot/v1/sensor/qry?id=xxx
#明確請求方式Request Method-只能採用GET(查詢規範上)
@app.route('/iot/v1/sensor/qry',methods=['GET'])
def sensorQry():
    #如何擷取採用URL QueryString傳遞參數??? Local Proxy代理一個request物件
    sensorId=request.args.get('id')
    #串接CHT IoT服務(查詢)--呼叫自訂模組的function
    try:
        result=readLastData(sensorId)
        return result #預設狀態碼為200
    except Exception as ex:
        #回應值第二個 設定Response status code
        return {"code":400,"message":"CHT IOT服務有問題"},500 #要能夠序列化 list or dict or string

#新增紅外線人體感測器資料服務端點 path當作參數
#RESTful Service 感測器資料新增匝道服務點    
@app.route('/iot/v1/sensor/<sensorid>/st/<status>/rawdata',methods=["POST"])    
def sensorHCAdd(sensorid,status):
    #取得採用path當作參數 取得sensorid
    #透過datetime static now() property取出本地日期與時間
    today=datetime.now()  #static method
    #轉換成iso 8601 format
    iso8601Date=today.isoformat()
    data={"status":status,"locationtime":iso8601Date}
    #將dict序列化成json String
    jsonString=json.dumps(data)
    print(jsonString)
    #呼叫自訂模組
    result=sensorTextDataWrite(sensorid,jsonString)
    return result


#主程式Entry Point
if __name__=='__main__':
    #啟動網站系統 透過Flask個體物件
    
    
    app.run('192.168.10.66',port=5566)