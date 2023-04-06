# Web Crawler
import requests

# Date Time
import datetime

import pandas as pd
from io import StringIO
# Finance
import talib

# 取得最近N天的股價，直接回傳DataFrame
def getStockData(stockId, days):

    # 設定要爬的時間
    start = datetime.datetime.now() - datetime.timedelta(days=days) 
    end = datetime.datetime.now()

    initial = datetime.datetime.strptime( '1970-01-01' , '%Y-%m-%d' )
    days = 24 * 60 * 60    #一天有86400秒 
    period1 = start - initial
    period2 = end - initial
    s1 = period1.days * days
    s2 = period2.days * (days + 1)

    # 添加header
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{stockId}.TW?period1={str(s1)}&period2={str(s2)}&interval=1d&events=history&includeAdjustedClose=true"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    response = requests.get(url,headers = headers)

    # 找不到資料回傳None
    if response.status_code == 404:
        return None
    
    df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])
    
    '''
    新增需要的資訊
    '''

    # KD
    df['k'], df['d'] = talib.STOCH(df['High'], 
                                            df['Low'], 
                                            df['Close'], 
                                            fastk_period=9,
                                            slowk_period=3,
                                            slowk_matype=0,
                                            slowd_period=3,
                                            slowd_matype=0)
    return df

# 代號、名稱存入字典回傳
def getTwStocks():

    response = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
    df = pd.read_html(response.text)[0]
    # 設定column名稱
    df.columns = df.iloc[0]
    # 刪除第一行
    df = df.iloc[2:]

    # 存入字典
    stockDict = {}

    for data in df['有價證券代號及名稱']:
        if len(data.split()[0]) != 4:
            continue
        stockDict[data.split()[0]] = data.split()[1]

    return stockDict

