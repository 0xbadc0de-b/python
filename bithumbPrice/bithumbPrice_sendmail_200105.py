#!C:\Python27\python.exe 

import time
import urllib
import simplejson
import ctypes

def sendMail():
	import smtplib
	from email.MIMEMultipart import MIMEMultipart
	from email.MIMEBase import MIMEBase
	from email.MIMEText import MIMEText
	import os

	user = ''	# email address
	pswd = ''	# email password
	text = ''	# message

	msg = MIMEMultipart()
	msg['From'] = user
	msg['To'] = ''		# receive mail address
	msg['Subject'] = ''	# mail title
	msg.attach(MIMEText(text))

	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(user, pswd)
	mailServer.sendmail(user, 'send email address', msg.as_string())
	mailServer.close()


# 2019-12-13 today price
maxBTC = 8800000
minBTC = 8200000
maxETH = 160000
minETH = 150000
maxEOS = 4000
minEOS = 3000
maxXRP = 300
minXRP = 200

coinList = ['BTC', 'ETH', 'EOS', 'XRP']
apiUrl = "https://api.bithumb.com/public/ticker/"

coinPrice = []
now = time.localtime()
now_date = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
now_time = "%02d:%02d" % (now.tm_hour, now.tm_min)

f = open("D:\\CodeTest\\bithumbPrice\\bithumb_coin_price_10min.log", 'a')

for coin in coinList:    
	coinApi = apiUrl + coin
	result = simplejson.load(urllib.urlopen(coinApi))
	result = result['data']['closing_price'].split(".")[0]    
	coinPrice.append(result)

nowPrice = now_date+"\t"+now_time+"\t"+coinPrice[0]+"\t"+coinPrice[1]+"\t"+coinPrice[2]+"\t"+coinPrice[3]
f.write(nowPrice+"\n")
f.close()

if int(coinPrice[0]) >= maxBTC or int(coinPrice[0]) <= minBTC or int(coinPrice[1]) >= maxETH or int(coinPrice[1]) <= minETH or int(coinPrice[2]) >= maxEOS or int(coinPrice[2]) <= minEOS or int(coinPrice[3]) >= maxXRP or int(coinPrice[3]) <= minXRP:
# if int(coinPrice[0]) >= maxBTC or int(coinPrice[0]) <= minBTC:
	# execute third-party program without cmd shell
	sendMail()

del coinPrice
