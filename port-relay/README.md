# 포트 포워딩(port forwarding) 분석 - port relay

## python 코드로 이해하기

python port relay 구글링해서 아래 github 발견 (READMD 설명쉬움)

https://github.com/strizhov/tcp-relay-python

virtualbox 3개 준비해서 아래처럼 구축

Client(telnet 사용) --- [8889p]Relay Server[8888p] --- Echo Server

![image](https://github.com/0xbadc0de-b/port-relay/blob/master/python/port%20relay.PNG)

relayserver.py 소스코드 분석하면

소켓을 2개 만듬

recv / send 를 사용해서 통신내용을 그대로 전달

해당 소스코드 주석달아서 첨부하였으니 참고하자

