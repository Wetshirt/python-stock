# Request
import crawler as craw


import time

# Algorithm
import algorithm as alg

import pandas as pd

import csv



'''
todo list:
    1. timer
    2. multiprocess
'''
def main():
    # get all stock id
    Stocks = craw.getTwStocks()
    recommendStocks = {}
    for s in Stocks:
        print("seq:", s)

        try:
            # 抓取最近30天的資料
            # getStockData(stockId, 30)
            df = craw.getStockData(s, 60)
            if df is None:
                continue
            if alg.isStrongBuy(df):
                recommendStocks[s] = list(df['Volume'].tail(1))[0]
        except:
            print("Error: Step Over!!")
            # 避免爬蟲次數太快被擋住
            time_duration = 90
            time.sleep(time_duration)

    recommendStocks = sorted(recommendStocks.items(), key=lambda x:x[1], reverse=True)
    recommendStocks = dict(recommendStocks)

    # save result to csv
    with open('res.csv', 'w', newline='') as f:  
        writer = csv.writer(f)
        writer.writerow(['代號', '成交量', '網址'])
        for k, v in recommendStocks.items():
            writer.writerow([k, v, f'https://www.cmoney.tw/forum/stock/{k}'])

if __name__ == '__main__':
    time_start = time.time() #開始計時

    main()

    time_end = time.time()    #結束計時
    time_c= time_end - time_start   #執行所花時間
    print('time cost', time_c, 's')
