import pandas as pd
from io import StringIO

# Finance
import talib

# Visual
import matplotlib.pyplot as plt
import mplfinance as mpf

import crawler as craw

def drawCharts(stockId):
    
    df = craw.getStockData(stockId, 30)

    # 繪圖
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    s  = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
    add_plot =[mpf.make_addplot(df["k"],panel= 2,color="b"),
            mpf.make_addplot(df["d"],panel= 2,color="r")]
    kwargs = dict(type='candle', mav=(5,10), volume = True,figsize=(20, 10),title = "Blue: K, Red: D", style=s,addplot=add_plot)
    mpf.plot(df, **kwargs)

drawCharts(2609)