from pybithumb import Bithumb
import ccxt
from bs4 import BeautifulSoup
import urllib.request as req
import re
import pyupbit

#업비트 BTC 가격
price_upbit_btc = pyupbit.get_current_price("KRW-BTC")

#바이낸스 BTC가격
binance = ccxt.binance()
ticker = binance.fetch_ticker('BTC/USDT')
price_btc_usdt = int(ticker['close']) # 미국 BTC 가격

#빗썸 BTC 가격
price_bithumb_btc = int(Bithumb.get_current_price("BTC"))

# 원달러 환율
url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
abc = soup.select_one("div.head_info > span.value").string
price_usd_krw = int(re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", abc)) / 100 # 1,400.00 > 1400 형변환 및 특수문자 처리


price_btc_krw_usdt = price_usd_krw * price_btc_usdt # 바이낸스 BTC 가격 KRW로 변환

#Bithumb 김프
kimp_bithumb =((price_bithumb_btc - price_btc_krw_usdt) / price_btc_krw_usdt ) * 100

#Upbit 김프
kimp_upbit =((price_upbit_btc - price_btc_krw_usdt) / price_btc_krw_usdt ) * 100

print("↓↓↓↓빗썸김프↓↓↓↓")
print(kimp_bithumb)
print("↓↓↓↓업비트김프↓↓↓↓")
print(kimp_upbit)