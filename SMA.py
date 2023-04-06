import crawler as craw

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

'''
簡單移動平均線高於指數移動平均線為多頭市場信號。
指數移動平均線高於簡單移動平均線為空頭市場信號。

SMA > EMA: Buy
EMA > SMA: Sell
'''


df = craw.getStockData(2388, 50)

# 計算簡單移動平均線和指數移動平均線
df['SMA'] = df['Close'].rolling(window=20).mean()
df['EMA'] = df['Close'].ewm(span=20, adjust=False).mean()

# 計算收益率
df['Returns'] = np.log(df['Close'] / df['Close'].shift(1))

# 計算交易信號
df['Signal'] = np.where(df['SMA'] > df['EMA'], 1, 0)

# 計算持有頭寸
df['Position'] = df['Signal'].diff()

# 計算策略收益率
df['Strategy'] = df['Position'] * df['Returns']

# 計算累計收益率
df['Cumulative_Returns'] = np.exp(df['Strategy'].cumsum()) - 1

# 繪製圖表
fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(df.index, df['Close'], label='Close')
ax.plot(df.index, df['SMA'], label='SMA')
ax.plot(df.index, df['EMA'], label='EMA')

ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()

plt.show()

print(df)