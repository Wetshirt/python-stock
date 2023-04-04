# Intro

紀錄python分析台股的過程


# 爬蟲

## [crawler.py](crawler.py)

1. 列出台股代號
2. 爬取個股資訊

### 列出台股代號 getTwStocks()

[如何獲得上市上櫃股票清單](https://www.finlab.tw/python%EF%BC%9A%E5%A6%82%E4%BD%95%E7%8D%B2%E5%BE%97%E4%B8%8A%E5%B8%82%E4%B8%8A%E6%AB%83%E8%82%A1%E7%A5%A8%E6%B8%85%E5%96%AE/)

從[這裡](http://isin.twse.com.tw/isin/C_public.jsp?strMode=2)取得台股代號

### 爬取近N天個股資訊 getStockData(stockId, days)

[抓取個股資料](https://chenchenhouse.com/python001/)

yahoo finance爬取

>request次數太快疑似會被擋住90秒 !!

# 分析

# 回測

# Todo

# Reference

[如何獲得上市上櫃股票清單](https://www.finlab.tw/python%EF%BC%9A%E5%A6%82%E4%BD%95%E7%8D%B2%E5%BE%97%E4%B8%8A%E5%B8%82%E4%B8%8A%E6%AB%83%E8%82%A1%E7%A5%A8%E6%B8%85%E5%96%AE/)

[抓取個股資料](https://chenchenhouse.com/python001/)