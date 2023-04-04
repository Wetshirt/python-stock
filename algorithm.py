
def isStrongBuy(df):

    if not filterKD(df['k'], df['d']):
        return False

    return True
'''
source: https://www.cmoney.tw/learn/course/technicals/topic/484

K 值 > D 值：上漲行情，適合做多
D 值 > K 值：下跌行情，適合空手或做空

D > 80: 超買區
D < 20: 超賣區
D = 50: 多空平衡

'''
def filterKD(K, D):
    k_value = list(K.tail(1))[0]
    d_value = list(D.tail(1))[0]

    # 超買 or 下跌行情
    if (d_value > 30) or (d_value > k_value):
        return False
    return True