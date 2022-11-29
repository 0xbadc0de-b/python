#!C:\Python27\python.exe 

import time
import urllib
import simplejson

coinList = ['BTC', 'ETH', 'EOS', 'XRP']
apiUrl = "https://api.bithumb.com/public/ticker/"

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
# print("\nDate\t\tTime\tBTC\tETH\tEOS\tXRP")
# print(nowPrice)
f.write(nowPrice+"\n")
f.close()

del coinPrice
