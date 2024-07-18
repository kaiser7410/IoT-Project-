#連接上資料庫 引用pymssql
import pymssql
#定義連接上資料庫相關屬性
server="localhost"
userName="sa"
password="1111"
databaseName="IoTDB"

#主程式
if __name__=='__main__':
    #使用模組connect function建立連接資料庫的連接物件
    connection=pymssql.connect(server,userName,password,databaseName)
    print(type(connection)) #連接物件
    #已經開啟的連接物件產生命令物件 Cursor
    #cursor命令物件(具有緩存 ACID-ON Transaction)
    cursor=connection.cursor()
    try:
        print(type(cursor))
        cursor.execute("Insert Into LineUser(UserId,Name,PictureURL) values(%s,%s,%s)",('U999991','張泰山','http://www.cht.com.tw'))
        connection.commit() #正式交付
    except:
        print('異動不成功 資料進行rollback')
        connection.rollback() #從log file到回來 回到原點   


   
