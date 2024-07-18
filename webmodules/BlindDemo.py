#控制樹莓派
import RPi.GPIO as rpi
import time #時鐘器
#定義OUPUT腳位 
PIN=14
#主程式
if __name__=='__main__':
    #設定樹莓派板子模式borad or bcm
    rpi.setmode(rpi.BCM)
    #設定output腳位
    rpi.setup(PIN,rpi.OUT)
    #進入無窮盡迴圈
    while True:
        #輸出通電
        rpi.output(PIN,1)
        #停一下
        time.sleep(2)
        rpi.output(PIN,0)
        time.sleep(2)

