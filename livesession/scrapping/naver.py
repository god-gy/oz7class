from unittest import result
import requests
from bs4 import BeautifulSoup

keywords = input("검색어를 입력해주세요: ")
url = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keywords}"
# 쿼리 뒤에 원하는 검색 키워드만 입력할 수 있는 상태면 너무 좋겠다! - 서비스 개선

rep = requests.get(url)  # get:기능의 이름. + 실행시킨다는 의미로()
# 위 코드를 실행하면 사이트를 구성할때 필요한 html,css,js 코드를 서버가 준다.

# 웹 코드가 뭔지 중요하지 않음 -> 데이터 타입으로만 구분함. => 문서 또는 글자(텍스트)로 판단함.
html = rep.text

# 받아온 html,css,js 코드를 python은 이해하지 못함. => 번역을 도와줄 조력자가 필요함.
soup = BeautifulSoup(html, "html.parser")   # html에서 사용된 모든 태그의 유형을 알려준다.

result = soup.select(".sds-comps-vertical-layout.sds-comps-full-layout.IoSVvu2hEbI_In6t6FAw") # 괄호 안엔 클래스명
# list와 동일한 형태의 데이터 타입
# select 문은 동일한 클래스명을 한번에 추출할때 사용된다.

for i in result:
    # 광고 제외 시키기
    ad = i.select_one(".vZ_ErVj5n5d07m6XzhoL")
    if not ad:
        # 제목, 링크, 작성자, 글요약
        title = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1.sds-comps-text-weight-sm").text
        writer = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1").text
        dsc = i.select_one(".sds-comps-text.sds-comps-text-type-body1.sds-comps-text-weight-sm").text
        link = i.select_one(".ialLiYPc7XEN3dJ4Tujv.pHHExKwXvRWn4fm5O0Hr")["href"]

        # 블로그 글 요약
        print(f"제목 : {title}")
        print(f"작성자 : {writer}")
        print(f"내용 : {dsc}")
        print(f"링크 : {link}")
        print()
