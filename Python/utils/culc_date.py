import datetime

def culc_year() :
    # 年度計算
    today = datetime.date.today()  
    if 4 <= today.month <= 12 :
        thisyear = today.year
    else :
        thisyear = today.year - 1
    return thisyear