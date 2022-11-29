#!python3

import cx_Oracle
 
#첫번째꺼로 하면 odbc 32bit 찾을수 없다고 오류남
#oracle 사이트에서 아래 2번째꺼로 odbc 32bit 라이브러리 다운받았음
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin")
cx_Oracle.init_oracle_client(lib_dir=r"D:\work\CodeTest\Python\instantclient_21_7")


# 사용자명/패스워드@서버ip:포트/접속할DB
con = cx_Oracle.connect('book_ex/book_ex@127.0.0.1:1521/XE')
cur = con.cursor()
 
cur.execute('select * from tab')
 
for result in cur:
   print( result )
 
cur.close()
con.close()