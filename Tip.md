# 테스트


https://gbgg.tistory.com/entry/엑셀-지식iN-엑셀-숫자-앞에-0을-채우는-방법은
엑셀 숫자 앞에 0 채우기
	1. 셀서식 > 사용자지정 > 형식칸에 원하는 갯수만큼 '0' 채우기 => 예) 000000 전체 6자리로 앞에 0 채움
	2. TEXT 함수 사용
		사용예) =TEXT(B1, "0000")





# 오라클 커서(Cursor)
	SQL의 SELECT문을 사용하여 테이블에서 레코드를 가져올 때, SQL은 해당 조건을 만족하는 모든 레코드들을 전체로 리턴할 뿐, 이 결과로부터 첫번째 ROW, 두번째 ROW, 다섯번째 ROW 등을 구분하여 엑세스할 수는 없다. 하지만 경우에 따라서는 이렇게 한 ROW씩 엑세스할 필요가 있는데, 이때 사용하는 것이 커서(Cursor)이다. TSQL에서 DECLARE...CURSOR를 사용하여 커서를 만들 때, 이 커서는 SQL 서버의 메모리상에 존재하는 서버 커서이며, 커서 내에서 전후로 이동하며 엑세스하는 것이 가능하다.
	http://www.sqlprogram.com/Basics/sql-cursor.aspx


# Pip 오프라인 설치
https://spectrum20.tistory.com/entry/python-파이썬-패키지-Offline-설치-수동-설치
https://lazywon.tistory.com/66

	> python -m pip install 파일명.whl
	이렇게만 하면 의존성 패키지들을 설치할 수 없어 무진장 오류가 발생함

	★★★ 의존성 패키지까지 설치
	> mkdir 폴더명
	> pip download 패키지명 -d ./폴더명
	=> 이렇게 하면 해당 폴더에 관련 패키지가 모두 다운로드 됨

	이제 오프라인 설치해보자
	> cd 폴더명
	> pip install 패키지명.whl -f ./ --no-index





# IDA Pro

https://haerinn.tistory.com/56#5. Stack Frame 확인하기
호출 함수 보기 : 원하는 함수(예: main) 위치에서 메뉴의 View-> Open subviews -> Function calls




# Q-Dir
	F7	: 탐색기 창에 전체경로 트리 보여줌



# PPT 템플릿 사이트
- 미리캔버스 [MiriCanvas]
- 캔바 [Canva]
- 올피피티 [ALLPPT]
- 슬라이드 카니발 [Slides Carnival]
- 슬라이드니스트 [Slidenest]
- 슬라이더고 [Slidesgo]





드림핵 cookie 문제


# VRAM 늘리기
https://blog.naver.com/richardsky9/222073316451
	방법1) BIOS에서 설정
	방법2) 레지스트리에서 설정


