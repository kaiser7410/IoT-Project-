#紅外線感測器 偵測區域內有人進來麻 
import RPi.GPIO as rpi  #Raspberry通用腳位模組
import time
import requests #Http Client
#全域變數設定設定(感測器腳位/板子腳位模式BCM)
#自己開發雲端服務主機位置
iotHosted='http://192.168.10.66:5566/iot/v1'
sensorID='HCSR01'

LEDPIN=14 #bcm
PIRPIN=15
#區域有人進來狀態碼
isAlarm=False
#設定腳位模式board or bcm
rpi.setmode(rpi.BCM) #取常數 命名大寫
#設定GPIO(Input/output)
rpi.setup(LEDPIN,rpi.OUT)
rpi.setup(PIRPIN,rpi.IN) #讀取紅外線感測寫進來的訊息  

#主程式
if __name__=='__main__':

    #進行迴圈無窮盡執行偵測
    #讀取紅外線感測狀態 true
    while True:
        try:
            if rpi.input(PIRPIN):

                #送出訊息到雲端(自訂服務)
                state='in'
                urlString=f'{iotHosted}/sensor/{sensorID}/st/{state}/rawdata'
                requests.post(urlString)
                print('有物件移動中...')
                #LED亮
                rpi.output(LEDPIN,rpi.HIGH)
                #紀錄現況狀態碼
                isAlarm=True
            else:
                #離開 或者是沒有人進來
                state='out'
                urlString=f'{iotHosted}/sensor/{sensorID}/st/{state}/rawdata'
                requests.post(urlString)
                #LED關閉
                if isAlarm:
                    print('人離開了...')
                    rpi.output(LEDPIN,rpi.LOW)    
                    #還原狀態
                    isAlarm=False
            time.sleep(2) #單位是秒數
        except:
            print('自訂服務沒有啟動!!或者連接不上...')       

    