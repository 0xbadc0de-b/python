#!C:\Python27\python.exe 

import sys
import time
import urllib
import simplejson
from colorama import init, Fore, Back, Style
init(autoreset=True)


coinList = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP']
apiUrl = "https://api.bithumb.com/public/ticker/"
timeCnt = 1
lineCnt = 1

print("----------------------------------------------------------------------")
print(Fore.CYAN + Style.BRIGHT + "bithumbPrice Ver 17.05.25 (May 25 2017)")
print(Fore.CYAN + Style.BRIGHT + "write by 0xBADC0DE. All rights reserved.")
print("----------------------------------------------------------------------")
time.sleep(2)
print("\nDate\t\tTime\tBTC\tETH\tDASH\tLTC\tETC\tXRP")
print("======================================================================")

try:    
    while True:
        coinPrice = []
        now = time.localtime()
        now_date = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
        now_time = "%02d:%02d" % (now.tm_hour, now.tm_min)

        f = open("bithumb_coin_price.log", 'a')
        
        for coin in coinList:    
            coinApi = apiUrl + coin
            
            result = simplejson.load(urllib.urlopen(coinApi))
            result = result['data']['closing_price'].split(".")[0]    
            coinPrice.append(result)

        nowPrice = now_date+"\t"+now_time+"\t"+coinPrice[0]+"\t"+coinPrice[1]+"\t"+coinPrice[2]+"\t"+coinPrice[3]+"\t"+coinPrice[4]+"\t"+coinPrice[5]

        if(timeCnt == 5):
            print(Fore.YELLOW + Style.BRIGHT + nowPrice)
            f.write(nowPrice+"\n")
            f.close()        
            timeCnt = 1
        else:
            print(nowPrice)            
            timeCnt = timeCnt + 1            
        
        time.sleep(30)

        if(lineCnt == 30):
            print("----------------------------------------------------------------------")
            print(Fore.CYAN + Style.BRIGHT + "bithumbPrice Ver 17.05.25 (May 25 2017)")
            print(Fore.CYAN + Style.BRIGHT + "write by 0xBADC0DE. All rights reserved.")
            print("----------------------------------------------------------------------")
            time.sleep(2)
            print("\nDate\t\tTime\tBTC\tETH\tDASH\tLTC\tETC\tXRP")
            print("======================================================================")
            lineCnt = 0

        lineCnt = lineCnt + 1
        del coinPrice
            
        
except KeyboardInterrupt:
    f.close()
    print("\nGood bye~~")
    sys.exit()
    
    



