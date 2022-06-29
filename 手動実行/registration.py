import sqlite3
import pandas as pd
import datetime

'''
DB登録
'''
today = datetime.date.today()  

if 4 <= today.month <= 12:
    thisyear = today.year
else :
    thisyear = today.year - 1

thismonth = today.month
if thismonth == 1:
    thismonth = 12
else:
    thismonth = thismonth - 1
print(thismonth)
    
if 1 <= thismonth <= 3:
    tmp = str(thisyear+1) + '0' + str(thismonth) + '.csv'
    df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\\成果物\\Python\\csv\\' + str(thisyear) + '\\' + str(tmp), encoding = 'UTF-8')
elif 4 <= thismonth <= 9:
    tmp = str(thisyear) + '0' + str(thismonth) + '.csv'
    df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\\成果物\\Python\\csv\\' + str(thisyear) + '\\' + str(tmp), encoding = 'UTF-8')
elif 10 <= thismonth <= 12:
    tmp = str(thisyear) + str(thismonth) + '.csv'
    df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\\成果物\\Python\\csv\\' + str(thisyear) + '\\' + str(tmp), encoding = 'UTF-8')


df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '拠点': 'site', '事象': 'phenomenon', '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})

# DB名取得
dbname = 'C:\\Users\\h4869\\Desktop\\TEST\\成果物\\Python\\DB\\Infra'
# DB接続
con = sqlite3.connect(dbname)

df_new.to_sql('incident', con, if_exists='append', index = 0) 
  
con.close()


'''
重複データを削除
'''
con = sqlite3.connect('dbname')
df_db = pd.read_sql('SELECT * FROM incident', con)
df_delete = df_db.drop_duplicates(subset=['number', 'service', 'site', 'phenomenon', 'cause', 'start', 'finish', 'status'])
df_delete.to_sql('incident', con, if_exists='replace', index = 0) 
