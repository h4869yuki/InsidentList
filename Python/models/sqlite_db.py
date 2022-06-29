from calendar import month
from distutils.util import execute
from itertools import count
import sqlite3
import datetime

today = datetime.date.today()  
if 4 <= today.month <= 12 :
    thisyear = today.year
else :
    thisyear = today.year - 1

def replace_to_dict(cursor, row):
    '''
    辞書型に変換
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_table(page, thisyear):
    '''
    今年度の全体/障害/作業/借用テーブルをそのまま取得
    '''
    con = sqlite3.connect('C:\\Users\\h4869\\Desktop\\TEST\\成果物\\Python\\DB\\Infra')
    con.row_factory = replace_to_dict
    cur = con.cursor()

    year_to_date = str(thisyear) + '/04/01' 
    year_from_date = str(thisyear + 1) + '/03/31'

    if page == 'top':
        cur.execute("SELECT * FROM incident WHERE start BETWEEN ? AND ?", [year_to_date, year_from_date])
        records = cur.fetchall()
        return records
    else:
        cur.execute("SELECT * FROM incident WHERE phenomenon=? AND start BETWEEN ? AND ?", [page, year_to_date, year_from_date])
        records = cur.fetchall()
        return records

def get_anualamount(page, thisyear):
    '''
    今年度の月毎の 全体/障害/作業/借用 件数を取得
    '''
    con = sqlite3.connect('C:\\Users\\h4869\\Desktop\\TEST\\成果物\\Python\\DB\\Infra')
    cur = con.cursor() 
    res_total = []
    res = []

    if page == 'top':
        for i in range(12) :
        # i には月が入る
            i += 1
            if 1 <= i <= 3 :
                # 年度に変換
                thisyear = thisyear + 1
                # 抽出条件
                year_and_month = str(thisyear) + '/' + str(i) + '/' + '%%'

                # クエリ実行
                cur.execute("SELECT COUNT(*) FROM incident WHERE start LIKE ?", [year_and_month])
                amount = cur.fetchall()

                # 月毎の●●の総数をリストに追加
                amount = str(amount).replace('[(','').replace(',)]','')
                res_total.append(int(amount))

                thisyear = thisyear - 1
            else :
                year_and_month = str(thisyear) + '/' + str(i) + '/' + '%%'
                cur.execute("SELECT COUNT(*) FROM incident WHERE start LIKE ?", [year_and_month])
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
                year_and_month = str(thisyear) + '/' + str(i) + '/' + '%%'

                # クエリ実行
                cur.execute("SELECT COUNT(*) FROM incident WHERE phenomenon=? AND start LIKE ?", [page,year_and_month])
                amount = cur.fetchall()

                # 月毎の障害/作業/借用の総数をリストに追加
                amount = str(amount).replace('[(','').replace(',)]','')
                res.append(int(amount))

                thisyear = thisyear - 1
            else :
                year_and_month = str(thisyear) + '/' + str(i) + '/' + '%%'

                cur.execute("SELECT COUNT(*) FROM incident WHERE phenomenon=? AND start LIKE ?", [page,year_and_month])
                amount = cur.fetchall()
                    
                amount = str(amount).replace('[(','').replace(',)]','')
                res.append(int(amount))
        return res

