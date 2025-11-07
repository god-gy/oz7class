'''
    kream 사이트 크롤링
'''

# 파이썬 기본 패키지
import time
import pymysql

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# class, id를 css_select를 이용해서 컨트롤하기 위한 패키지
from selenium.webdriver.common.by import By
# 키보드의 입력 형태를 코드로 작성해서 열려있는 크롬에게 전달하기 위한 패키지
from selenium.webdriver.common.keys import Keys

url = "https://kream.co.kr"

# 테스트용 크롬 브라우저에 옵션 적용
option_ = Options()
option_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option_)
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(1)
# 여기까지가 돋보기를 누르고 검색을 할 수 있도록 만드는 코드였습니다.

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

for item in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


# ------------------혼자해보기-------------------
# items = soup.select(".product_card")

# for item in items:
#     product_name = item.select_one(".text_body.pc\:w-fill").text
#     product_price = item.select_one(".price-info-container.pc\:w-fill").text

#     print(f'제품명 : {product_name}')
#     print(f'제품 가격 : {product_price}')
# ---------------------------------------------



# ------------------강의들으며 해보기-------------------
# ^= : 시작이 일치하는걸 찾아줘
# $= : 끝 일치하는걸 찾아줘
# *= : 포함하는걸 찾아줘
items = soup.select('a.product_card[data-sdui-id^="product_card/"]')

product_list = []

for item in items:

    category = "상의"

    # #text-element, text-lookup, display_paragraph 세 클래스를 모두 가진 <p> 요소들 중에서 semibold 클래스가 없는(즉 굵게 처리되지 않은) 요소를 선택하라는 뜻이에요.
    # 제품명: 카드 내부, 굵지 않은 제목이고 <p> 태그를 갖고 있는 것.
    name = item.select_one('p.text-element.text-lookup.display_paragraph:not(.semibold)')
    product_name = name.get_text(strip=True)    # 공백 제거

    if "후드" in product_name:

        # 브랜드 : 같은 pid를 가진 별도 블록에서 굵은 <p>
        # data-sdui-id 속성이 "product_brand_name/"로 시작하는 요소 안에 포함된, semibold 클래스를 가진 <p> 요소를 선택하라는 뜻이에요.
        brand = item.select_one('[data-sdui-id^="product_card/"] p.semibold')
        product_brand = brand.get_text(strip=True)

        # 가격 : 카드 내부 가격 블록에서 굵은 <p>
        #.price-info-container 안쪽의 .label-text-container 영역에 어디엔가 포함되어 있는 semibold 클래스를 가진 <p> 요소를 선택하라는 뜻이에요.
        price = item.select_one(".price-info-container .label-text-container p.semibold")
        product_price = price.get_text(strip=True)

        # print(f'카테고리 : {category}')
        # print(f'브랜드 : {product_brand}')
        # print(f'제품명 : {product_name}')
        # print(f'제품 가격 : {product_price}')
        # print()

        product_info = [category, product_brand, product_name, product_price]
        product_list.append(product_info)
# ------------------------------------------------

driver.quit()

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="20241013",
    db="kream",
    charset="utf8mb4"
)

def execute_query(conn, query, args=None):
    with conn.cursor() as cursor:
        cursor.execute(query, args or ()) # select * from kream3
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()

for i in product_list:
    execute_query(connection, "INSERT INTO KREAM (category, product_brand, product_name, product_price) VALUES (%s, %s, %s, %s)",(i[0],i[1],i[2],i[3]))
