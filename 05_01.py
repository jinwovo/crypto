from pybithumb import Bithumb
import ccxt
from bs4 import BeautifulSoup
import urllib.request as req
import re

#바이낸스 BTC가격
binance = ccxt.binance()
ticker = binance.fetch_ticker('BTC/USDT')

# 원달러 환율
url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

abc = soup.select_one("div.head_info > span.value").string #미국 원달러 환율
price_usd_krw = int(re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", abc)) / 100

price_btc_krw = int(Bithumb.get_current_price("BTC")) # 한국 BTC 가격

price_btc_usdt = int(ticker['close']) # 미국 BTC 가격

price_btc_krw_usdt = price_usd_krw * price_btc_usdt

kimp =((price_btc_krw - price_btc_krw_usdt) / price_btc_krw_usdt )*100 #kimp 가격

print(kimp)