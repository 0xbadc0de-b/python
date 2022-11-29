# -*- coding: utf-8 -*-
'''
# 작성자 : 0xBADC0DE
# 작성일 : 2018-12-31
# 개발환경 : python 2.7.x

# 기능: 
    - 同 도구는 성명학 81수리 중에서 좋은이름과 부자되는 이름의 경우의 수를 추출한다.
    - 한글 이름을 먼저 정한후 同 도구에서 추출된 81수리 경우의 수와 매칭되는 한자를 한자사전에서 찾아서 이름을 짓자.

# 81수리 계산 참고사항
    - 원격(元格) : [name2 + name3] 초년운, 이름(상명자와 하명자)의 획수를 합한 수
    - 형격(亨格) : [name1 + name2] 청년운, 성과 상명자 (이름 첫자)의 획수를 합한 수
    - 이격(利格) : [name1 + name3] 장년운, 성과 하명자 (이름 둘째자)의 획수를  합한 수
    - 정격(貞格) : [name1 + name2 + name3] 인생총운, 총격(總格). 성과 상명자, 하명자의 획수를 모두 합한 수
'''

# 스마트폰 작명앱(넴유베)ㆍ인터넷 검색한 81수리중 매우나쁨ㆍ보통수 모음 (45개)
bad_num = [2,4,9,10,12,14,19,20,22,26,27,28,30,34,36,40,42,43,44,46,49,50,51,53,54,55,56,58,59,60,62,64,66,69,70,71,72,73,74,75,76,77,78,79,80]
# 넴유베ㆍ인터넷에서 검색한 매우좋음 모음 (36개)
good_num = [1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,29,31,32,33,35,37,38,39,41,45,47,48,52,57,61,63,65,67,68,81]
# 넴유베ㆍ인터넷에서 검색한 81수리중 부자되는 숫자 (25개)
rich_num = [1,3,5,6,11,15,21,23,24,25,31,32,33,37,39,41,45,47,48,57,61,63,65,67,81]

# 발음ㆍ수리오행의 결과중 매우좋음 모음
good_ohang = [
u"목화토",u"목수금",u"목목화",u"목화화",u"목수수",u"목목수",u"목화목",u"목수목",
u"화토금",u"화목수",u"화화토",u"화토토",u"화목목",u"화화목",u"화토화",u"화목화",
u"토금수",u"토화목",u"토토금",u"토금금",u"토화화",u"토토화",u"토금토",u"토화토",
u"금수목",u"금토화",u"금금수",u"금수수",u"금토토",u"금금토",u"금토금",u"금수금",
u"수목화",u"수금토",u"수수목",u"수목목",u"수금금",u"수수금",u"수금수",u"수목수"
]

def main():
  firstName = int(raw_input(u"성의 한자 획수(예: 方, 4획) : ".encode('euc-kr'))) #方(방, 4획)
  
  print("\n-----[ All good name ]-----")
  for i in suri_ohang(good_name(firstName)):
    print("%02d + %02d + %02d = %02d" %(i[0],i[1],i[2],i[3]))
    
  print("\n-----[ Rich name ]-----")
  for i in suri_ohang(rich_name(firstName)):
    print("%02d + %02d + %02d = %02d" %(i[0],i[1],i[2],i[3]))

##################################################################################
# good_name(), rich_name() 함수를 통해서 좋은이름ㆍ부자되는이름의 경우의 수 결과값을 얻은후  
# 좋은이름 및 부자되는 이름의 경우의 수에 수리오행을 적용한 최종 경우의 수를 출력한다.
#  - input   : (type:list) 경우의 수 모음 리스트
#  - output : (type:list) 인자값으로 넘어온 경우의 수 모음중 수리오행이 매우좋은 경우의 수만 모은 리스트
##################################################################################
def suri_ohang(tmpList):
  suri_ohang_result = []
  
  for i in tmpList:
    # print(i)
    luck_one = i[0] + i[2]    #이격(장년운)
    luck_two = i[0] + i[1]    #형격(청년운)
    luck_three = i[1] + i[2]  #원격(초년운)
    
    # print("%d/%d/%d" %(luck_one%10, luck_two%10, luck_three%10))
    # 한자 끝자리 획수를 구하기 위해서 10으로 나눈 나머지를 확인함
    tmp_ohang = suri_ohang_change(luck_one%10)
    tmp_ohang += suri_ohang_change(luck_two%10)
    tmp_ohang += suri_ohang_change(luck_three%10)
    
    try:
      # 한자 끝자리 획수를 한글로 변환한 내용이 수리오행 매우좋음 리스트에 있으면 해당 경우의 수는 출력
      good_ohang.index(tmp_ohang)
      # print("%02d + %02d + %02d = %02d" %(i[0],i[1],i[2],i[3]))
      suri_ohang_result.append(i)
    except:
      pass

  return suri_ohang_result

##################################################################################
# 한자 끝자리 획수를 수리오행 한글로 변환
#  - input   : (type:int) 한자 끝자리 획수
#  - output : (type:string) 획수를 오행으로 변환한 글자
##################################################################################
def suri_ohang_change(num):
  if num == 1 or num == 2:
    return u"목"
  elif num == 3 or num == 4:
    return u"화"
  elif num == 5 or num == 6:
    return u"토"
  elif num == 7 or num == 8:
    return u"금"
  elif num == 9 or num == 0:
    return u"수"

##################################################################################
# 원ㆍ형ㆍ이ㆍ정격 4개 모두가 '좋은이름'의 경우의 수를 만들어낸다.
#  - input   : (type:int) 성의 한자 획수
#  - output : (type:list) 81수리가 좋은이름의 경우의 수 리스트
##################################################################################
def good_name(firstName):
  good_num_result = []
  
  for midName in range(1,82):
    for lastName in range(1,82):
      try:
        # index 기능은 list에서 해당 항목이 몇번째 있는지 리턴한다. 
        # 만약 찾는 항목이 list에 없으면 except을 발생한다.
        good_num.index(midName+lastName)  # 원격이 좋으면 통과 and
        good_num.index(firstName+midName)  # 형격이 좋으면 통과 and
        good_num.index(firstName+lastName)  # 이격이 좋으면 통과 and
        good_num.index(firstName+midName+lastName)  # 정격이 좋으면 통과
        if (firstName+midName+lastName) < 82:
          # print("%02d + %02d + %02d = %02d" %(firstName, midName, lastName, firstName+midName+lastName))
          good_num_result.append((firstName, midName, lastName, firstName+midName+lastName))
      except:
        pass
        
  return good_num_result

##################################################################################
# 원ㆍ형ㆍ이ㆍ정격 4개 모두가 '부자되는 이름'의 경우의 수를 만들어낸다.
#  - input   : (type:int) 성의 한자 획수
#  - output : (type:list) 4개 운수가 모두 부자되는 이름의 경우의 수 리스트
##################################################################################
def rich_name(firstName):
  rich_num_result = []
  
  for midName in range(1,82):
    for lastName in range(1,82):
      try:
        rich_num.index(midName+lastName)  # 원격이 좋으면 통과 and
        rich_num.index(firstName+midName)  # 형격이 좋으면 통과 and
        rich_num.index(firstName+lastName)  # 이격이 좋으면 통과 and
        rich_num.index(firstName+midName+lastName)  # 정격이 좋으면 통과
        if (firstName+midName+lastName) < 82:
          # print("%02d + %02d + %02d = %02d" %(firstName, midName, lastName, firstName+midName+lastName))
          rich_num_result.append((firstName, midName, lastName, firstName+midName+lastName))
      except:
        pass
  
  return rich_num_result
          
if __name__=="__main__":
  main()
  