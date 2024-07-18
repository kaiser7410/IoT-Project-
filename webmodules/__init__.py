from flask import Flask
app=Flask('__main__') #參數命名 往往使用當下這一個模組

#進行網站模組 route 初始化
import webmodules.WebHookService
