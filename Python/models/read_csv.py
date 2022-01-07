import csv
import sqlite3
from numpy import number
import pandas as pd

def registration():
  df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\202112.csv', encoding = 'UTF-8')
  dbname = 'TEST.db'
  conn = sqlite3.connect(dbname)
  df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '事象': 'phenomenon', '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})
  df_new.to_sql('test_table', conn, if_exists='replace')
 
  conn.close()
registration()

def withdraw():
  dbname = 'TEST.db'
  conn = sqlite3.connect(dbname)
  df_db = pd.read_sql('SELECT * FROM test_table', conn)

  global df_db_list
  df_db_list = df_db['number'].to_list()
  df_db_count = (len(df_db_list))

  d_records = df_db.to_dict('records')
  
  conn.close()
  return d_records

def table_count():
  df_db_count = (len(df_db_list))
  return df_db_count












  # with open('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\data.csv', 'r', encoding='UTF-8') as f:
  #   h = next(csv.reader(f))
  #   csv_file = csv.reader(f)
  #   for row in csv_file :

  #     dbname = 'table.db'
  #     conn = sqlite3.connect(dbname)
  #     cur = conn.cursor()
  #     cur.executescript("CREATE TABLE IF NOT EXISTS table.db")
  #     conn.executemany("INSERT INTO table.db Values(?, ?, ?, ?, ?, ?, ?)", row)
  #     conn.commit()

  #     print(cur.fetchall())



      # dbname = 'table.db'
      # conn = sqlite3.connect(dbname)
      # cur = conn.cursor()
      # conn.executemany("INSERT INTO table.db VALUES(?,?,?,?,?,?,?)", [row[0],row[1],row[2],row[3],row[4],row[5],row[6]])

    
      
# def imp():
#   res = []
#   res_before = {}
#   with open('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\data.csv', 'r', encoding='UTF-8') as f:
#     h = next(csv.reader(f))
#     csv_file = csv.reader(f)
#     for line in csv_file :
#       res_before['number'] = line[0]
#       res_before['service'] = line[1]
#       res_before['phenomenon'] = line[2]
#       res_before['cause'] = line[3]
#       res_before['start'] = line[4]
#       res_before['finish'] = line[5]
#       res_before['status'] = line[6]
#       res.append(res_before)
#       res_before = {}
#     # return res
#     print(res)
# imp()