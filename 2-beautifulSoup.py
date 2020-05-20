#!python3
# -*- coding: utf-8 -*-
# (책소스) 파이썬으로 웹 크롤러 만들기
from urllib.request import urlopen
from bs4 import BeautifulSoup	#pip3 install beautifulsoup4

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)	#위 URL html중 <h1>만 추출해서 출력
