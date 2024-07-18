#引用
import pymssql
#常數
#定義連接上資料庫相關屬性
server=""
userName=""
password=""
databaseName="IoTDB"

#設計連接物件產生(具有Open)
def connectionOpen():
    #使用模組connect function建立連接資料庫的連接物件
    connection=None
    try:
        connection=pymssql.connect(server,userName,password,databaseName)
    except Exception as ex:
        raise ex #拋出例外到應用系統
    return connection

#新增資料
#參數 注入互動連接物件
#參數2:新增SQL語法具有參數架構
#參數3:參數值tuple物件 
def insert(connection,sqlString,args):
    #cursor命令物件(具有緩存 ACID-ON Transaction)
    cursor=connection.cursor()
    try:
        cursor.execute(sqlString,args)
        connection.commit() #正式交付
    except Exception as ex:
        connection.rollback() #從log file到回來 回到原點  
        raise ex

#進行修改或者新增作業
#封鎖或者解鎖(修改)
#args 傳遞tuple物件 保留最後一個是條件
def update(connection,updateString,args):
    #透過connection產生一個Cursor物件
    try:
        cursor=connection.cursor() 
        #透過cursor執行sql命令
        cursor.execute(updateString,args) #啟動Transaction
        connection.commit() #正式完成更新資料
        #更新OK 
    except Exception as ex:
        connection.rollback() #資料全部倒回來
        raise ex #拋出例外到應用系統去

#查詢單筆作業
def queryForObject(connection,selectString,args):
    #透過connection產生一個Cursor物件
    try:
        cursor=connection.cursor() 
        #透過cursor執行sql命令(執行查詢 會產生資料庫那邊ResultSet),前端逐步Fetching一筆取下來
        cursor.execute(selectString,args)
        #取出相對記錄
        result=cursor.fetchone()
        return result
       
    except Exception as ex:
        raise ex #拋出例外到應用系統去    


   