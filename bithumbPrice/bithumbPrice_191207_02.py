#!C:\Python27\python.exe 

import time
import urllib
import simplejson
import ctypes

# 2019-12-07 today price
maxBTC = 8900000
minBTC = 8800000
maxETH = 175000
minETH = 173000
maxEOS = 3300
minEOS = 3100
maxXRP = 270
minXRP = 250

coinList = ['BTC', 'ETH', 'EOS', 'XRP']
apiUrl = "https://api.bithumb.com/public/ticker/"
showPriceList = False
coinPrice = []

now = time.localtime()
now_date = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
now_time = "%02d:%02d" % (now.tm_hour, now.tm_min)

f = open("D:\\CodeTest\\bithumbPrice\\bithumb_coin_price.log", 'a')

for coin in coinList:    
	coinApi = apiUrl + coin
	result = simplejson.load(urllib.urlopen(coinApi))
	result = result['data']['closing_price'].split(".")[0]    
	coinPrice.append(result)

nowPrice = now_date+"\t"+now_time+"\t"+coinPrice[0]+"\t"+coinPrice[1]+"\t"+coinPrice[2]+"\t"+coinPrice[3]
f.write(nowPrice+"\n")

if int(coinPrice[0]) >= maxBTC:
	showPriceList = True
	f.write("maxBTC = %d\n" %maxBTC)
if int(coinPrice[0]) <= minBTC:
	showPriceList = True
	f.write("minBTC = %d\n" %minBTC)
if int(coinPrice[1]) >= maxETH:
	showPriceList = True
	f.write("maxETH = %d\n" %maxETH)
if int(coinPrice[1]) <= minETH:
	showPriceList = True
	f.write("minETH = %d\n" %minETH)
if int(coinPrice[2]) >= maxEOS:
	showPriceList = True
	f.write("maxEOS = %d\n" %maxEOS)
if int(coinPrice[2]) <= minEOS:
	showPriceList = True
	f.write("minEOS = %d\n" %minEOS)
if int(coinPrice[3]) >= maxXRP:
	showPriceList = True
	f.write("maxXRP = %d\n" %maxXRP)
if int(coinPrice[3]) <= minXRP:
	showPriceList = True
	f.write("minXRP = %d\n" %minXRP)

if showPriceList:
	# execute third-party program without cmd shell
	ctypes.windll.shell32.ShellExecuteA(0, 'open', 'D:\\CodeTest\\bithumbPrice\\bithumb_coin_price.log', None, None, 1)

f.close()
del coinPrice

