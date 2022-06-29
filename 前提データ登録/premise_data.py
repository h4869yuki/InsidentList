import sqlite3
import pandas as pd

dbname = 'C:\\Users\\h4869\\Desktop\\TEST\\成果物\\Python\\DB\\Infra'
con = sqlite3.connect(dbname)
for i in range(4,10):
    tmp = '2022' + '0' + str(i) + '.csv'
    df= pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\\成果物\\Python\\csv\\2022\\' + str(tmp), encoding = 'UTF-8')
    df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '拠点': 'site', '事象': 'phenomenon', '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})
    df_new.to_sql('incident', con, if_exists='append', index = 0) 

for i in range(10,13):
    tmp = '2022' + str(i) + '.csv'
    df= pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\\成果物\\Python\\csv\\2022\\' + str(tmp), encoding = 'UTF-8')
    df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '拠点': 'site', '事象': 'phenomenon',  '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})
    df_new.to_sql('incident', con, if_exists='append', index = 0) 
con.close()
