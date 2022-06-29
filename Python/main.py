from os import name
from flask import Flask, render_template, make_response, jsonify
from flask import request

from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from werkzeug.utils import redirect
from models.sqlite_db import get_table
from models.sqlite_db import get_anualamount
import numpy as np
from datetime import date, timedelta
from utils.culc_date import culc_year


# インスタンスの生成
app = Flask(__name__)

def graph1():
    thisyear = culc_year()
    c_alert = get_anualamount('ALERT',thisyear)  
    c_work = get_anualamount('Work',thisyear)
    c_maintanance = get_anualamount('Maintanance',thisyear)
    plt.rcParams["font.family"] = "MS Gothic"
    x = ['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月'] 
    y = np.array([c_alert[3], c_alert[4], c_alert[5], c_alert[6], c_alert[7], c_alert[8], c_alert[9], c_alert[10], c_alert[11], c_alert[0], c_alert[1], c_alert[2]])
    y2 = np.array([c_work[3], c_work[4], c_work[5], c_work[6], c_work[7], c_work[8], c_work[9], c_work[10], c_work[11], c_work[0], c_work[1], c_work[2]])
    y3 = np.array([c_maintanance[3], c_maintanance[4], c_maintanance[5], c_maintanance[6], c_maintanance[7], c_maintanance[8], c_maintanance[9], c_maintanance[10], c_maintanance[11], c_maintanance[0], c_maintanance[1], c_maintanance[2]])
    fig, ax = plt.subplots(figsize=(9.5, 3.5))
    rect = ax.bar(x, y, width=0.8, label="アラート", color='y')
    rect = ax.bar(x, y2, bottom = y, width=0.8, label="作業", color='c')
    rect = ax.bar(x, y3, bottom = y + y2, width=0.8, label="メンテナンス", color='m')
    # today = date.today()
    # last_month = (today - timedelta(days=today.day)).month
    # rect[last_month-1].set_color('steelblue')
    plt.title("インシデント総計")
    plt.legend()

    plt.savefig("Python/static/img/top.png")
    plt.close()
graph1()

def graph2():
    thisyear = culc_year()
    page = 'ALERT'
    c_month = get_anualamount(page,thisyear)  
    plt.rcParams["font.family"] = "MS Gothic"
    x = ['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月'] 
    y = [c_month[3], c_month[4], c_month[5], c_month[6], c_month[7], c_month[8], c_month[9], c_month[10], c_month[11], c_month[0], c_month[1], c_month[2]] 
    fig, ax = plt.subplots(figsize=(9.5, 3.5))
    rect = ax.bar(x, y, width=0.8, label="アラート",  color='y')
    # today = date.today()
    # last_month = (today - timedelta(days=today.day)).month
    # rect[last_month-1].set_color('steelblue')
    plt.title("アラート件数")
    plt.legend()

    plt.savefig("Python/static/img/alert.png")
    plt.close()
graph2()

def graph3():
    thisyear = culc_year()
    page = 'Work'
    c_month = get_anualamount(page,thisyear)  
    plt.rcParams["font.family"] = "MS Gothic"
    x = ['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月'] 
    y = [c_month[3], c_month[4], c_month[5], c_month[6], c_month[7], c_month[8], c_month[9], c_month[10], c_month[11], c_month[0], c_month[1], c_month[2]] 
    fig, ax = plt.subplots(figsize=(9.5, 3.5))
    rect = ax.bar(x, y, width=0.8, label="作業", color='c')
    # today = date.today()
    # last_month = (today - timedelta(days=today.day)).month
    # rect[last_month-1].set_color('steelblue')
    plt.title("作業件数")
    plt.legend()

    plt.savefig("Python/static/img/work.png")
    plt.close()
graph3()

def graph4():
    thisyear = culc_year()
    page = 'Maintanance'
    c_month = get_anualamount(page,thisyear)  
    plt.rcParams["font.family"] = "MS Gothic"
    x = ['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月'] 
    y = [c_month[3], c_month[4], c_month[5], c_month[6], c_month[7], c_month[8], c_month[9], c_month[10], c_month[11], c_month[0], c_month[1], c_month[2]] 
    fig, ax = plt.subplots(figsize=(9.5, 3.5))
    rect = ax.bar(x, y, width=0.8, label="メンテナンス", color='m')
    # today = date.today()
    # last_month = (today - timedelta(days=today.day)).month
    # rect[last_month-1].set_color('steelblue')
    plt.title("メンテナンス件数")
    plt.legend()

    plt.savefig("Python/static/img/maintanance.png")
    plt.close()
graph4()

@app.route('/')
def index():
    graph4()
    return redirect('/top')

@app.route('/top')
def top():
    thisyear = culc_year()
    png = "static/img/top.png"
    page = "top"
    tbl_data = get_table(page,thisyear)
    anualamount = get_anualamount(page,thisyear)
    return render_template('index.html', tbl_data=tbl_data, anualamount=anualamount, png=png, thisyear=thisyear)

@app.route('/alert')
def alert():
    thisyear = culc_year()
    png = "static/img/alert.png"
    page = "ALERT"
    tbl_data = get_table(page,thisyear)
    anualamount = get_anualamount(page,thisyear)
    return render_template('index.html', tbl_data=tbl_data, anualamount=anualamount, png=png, thisyear=thisyear)

@app.route('/work')
def work():
    thisyear = culc_year()
    png = "static/img/work.png"
    page = "Work"
    tbl_data = get_table(page,thisyear)
    anualamount = get_anualamount(page,thisyear)
    return render_template('index.html', tbl_data=tbl_data, anualamount=anualamount, png=png, thisyear=thisyear)
    
@app.route('/maintanance')
def maintanance():
    thisyear = culc_year()
    png = "static/img/maintanance.png"
    page = "Maintanance"
    tbl_data = get_table(page,thisyear)
    anualamount = get_anualamount(page,thisyear)
    return render_template('index.html', tbl_data=tbl_data, anualamount=anualamount, png=png, thisyear=thisyear)

if __name__ == "__main__":
    app.run(debug=True)