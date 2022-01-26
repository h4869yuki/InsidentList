from calendar import month
from distutils.util import execute
from itertools import count
import sqlite3
from glob import glob
import pandas as pd
import datetime

today = datetime.date.today()  
if 4 <= today.month <= 12 :
    thisyear = today.year
else :
    thisyear = today.year - 1


def test():
    dbname = 'DB\Infra'
    con = sqlite3.connect(dbname)
    for i in range(4,10):
        tmp = '2021' + '0' + str(i) + '.csv'
        df= pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\2021\\' + str(tmp), encoding = 'UTF-8')
        df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '拠点': 'site', '事象': 'phenomenon', '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})
        df_new.to_sql('insident', con, if_exists='append', index = 0) 

    for i in range(10,12):
        tmp = '2021' + str(i) + '.csv'
        df= pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\2021\\' + str(tmp), encoding = 'UTF-8')
        df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '拠点': 'site', '事象': 'phenomenon',  '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})
        df_new.to_sql('insident', con, if_exists='append', index = 0) 
    con.close()
test()

def registration(thisyear):
    '''
    DB登録
    '''
    today = datetime.date.today()  
    thismonth = today.month
    if thismonth == 1:
        thismonth = 12
    else:
        thismonth - 1

    if 1 <= thismonth <= 3:
        tmp = str(thisyear+1) + '0' + str(thismonth) + '.csv'
        df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\' + str(thisyear) + '\\' + str(tmp), encoding = 'UTF-8')
    elif 4 <= thismonth <= 9:
        tmp = str(thisyear) + + '0' + str(thismonth) + '.csv'
        df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\' + str(thisyear) + '\\' + str(tmp), encoding = 'UTF-8')
    elif 10 <= thismonth <= 12:
        tmp = str(thisyear) + str(thismonth) + '.csv'
        df = pd.read_csv('C:\\Users\\h4869\\Desktop\\TEST\\Python\\csv\\' + str(thisyear) + '\\' + str(tmp), encoding = 'UTF-8')


    df_new = df.rename(columns={'管理番号': 'number', 'サービス': 'service', '拠点': 'site', '事象': 'phenomenon', '原因': 'cause',  '開始日時': 'start', '終了日時': 'finish', 'ステータス': 'status'})

  # DB名取得
    dbname = 'DB\Infra'
  # DB接続
    con = sqlite3.connect(dbname)

    df_new.to_sql('insident', con, if_exists='append', index = 0) 
  
    con.close()
registration(thisyear)


def delete_table():
    # ToDo 重複データを削除
    con = sqlite3.connect('DB\Infra')
    df_db = pd.read_sql('SELECT * FROM insident', con)
    df_delete = df_db.drop_duplicates(subset=['number', 'service', 'site', 'phenomenon', 'cause', 'start', 'finish', 'status'])
    df_delete.to_sql('insident', con, if_exists='replace', index = 0) 
delete_table()


# dict_factoryの定義
def dict_factory(cursor, row):
   d = {}
   for idx, col in enumerate(cursor.description):
       d[col[0]] = row[idx]
   return d

def get_annualdata(page, thisyear):
    '''
    DB一覧取得
    '''
    con = sqlite3.connect('DB\Infra')
    con.row_factory = dict_factory
    cur = con.cursor()

    tmp = str(thisyear) + '/04/01' 
    tmp2 = str(thisyear + 1) + '/03/31'
    
    if page == 'top':
        cur.execute("SELECT * FROM insident WHERE start BETWEEN ? AND ?", [tmp, tmp2])
        records = cur.fetchall()
        return records
    else:
        cur.execute("SELECT * FROM insident WHERE phenomenon=? AND start BETWEEN ? AND ?", [page, tmp, tmp2])
        records = cur.fetchall()
        return records

def count_month(page, thisyear):
    con = sqlite3.connect('DB\Infra')
    cur = con.cursor() 
    res_total = []
    res = []

    if page == 'top':
        for i in range(12) :
            i += 1
            if 1 <= i <= 3 :
                thisyear = thisyear + 1
                # 抽出条件
                tmp = str(thisyear) + '/' + str(i) + '/' + '%%'

                # クエリ実行
                cur.execute("SELECT COUNT(*) FROM insident WHERE start LIKE ?", [tmp])
                amount = cur.fetchall()

                # 月毎の●●の総数をリストに追加
                amount = str(amount).replace('[(','').replace(',)]','')
                res_total.append(int(amount))

                thisyear = thisyear - 1
            else :
                tmp = str(thisyear) + '/' + str(i) + '/' + '%%'
                cur.execute("SELECT COUNT(*) FROM insident WHERE start LIKE ?", [tmp])
                amount = cur.fetchall()
                    
                amount = str(amount).replace('[(','').replace(',)]','')
                res_total.append(int(amount))
            
        return res_total

    else :
        for i in range(12) :
            i += 1
            if 1 <= i <= 3 :
                thisyear = thisyear + 1
                # 抽出条件
                tmp = str(thisyear) + '/' + str(i) + '/' + '%%'

                # クエリ実行
                cur.execute("SELECT COUNT(*) FROM insident WHERE phenomenon=? AND start LIKE ?", [page,tmp])
                amount = cur.fetchall()

                # 月毎の●●の総数をリストに追加
                amount = str(amount).replace('[(','').replace(',)]','')
                res.append(int(amount))

                thisyear = thisyear - 1
            else :
                tmp = str(thisyear) + '/' + str(i) + '/' + '%%'

                cur.execute("SELECT COUNT(*) FROM insident WHERE phenomenon=? AND start LIKE ?", [page,tmp])
                amount = cur.fetchall()
                    
                amount = str(amount).replace('[(','').replace(',)]','')
                res.append(int(amount))
        return res

