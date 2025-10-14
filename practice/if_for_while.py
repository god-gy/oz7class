"""
    14-16강 실습문제 연습
"""
# 편의점 음료 관리 프로그램 만들기

import json
import unicodedata

def align_korean(text, width):
    """한글 포함 문자열을 일정 폭으로 정렬"""
    count = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ['F', 'W']:
            count += 2
        else:
            count += 1
    return text + ' ' * (width - count)

# json data 세팅
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        stock = data['stock']
        price = data['price']
        sales = data['sales']
    print("✅ 이전 데이터 불러오기 완료!")
except FileNotFoundError:
    print("⚠️ 저장된 데이터가 없습니다. 새로 시작합니다.")

    # 초기데이터
    stock = {
        '콜라': 10,
        '사이다': 8,
        '환타': 5
    }

    price = {
        '콜라': 1500,
        '사이다': 1300,
        '환타': 1400
    }

    sales = {
        '콜라': 0,
        '사이다': 0,
        '환타': 0
    }

# ==============================
# 🔹 메인 루프 시작
# ==============================

while True:
    print("\n===== 편의점 음료 관리 프로그램 =====")
    print("1. 음료 구매")
    print("2. 재고 및 매출 현황")
    print("3. 재고 관리 (추가/삭제)")
    print("4. 프로그램 종료")
    choice = input("원하는 작업의 번호를 입력하세요: ")

    # ------------------------------
    # 1️⃣ 음료 구매
    # ------------------------------

    if choice == '1':
        print("\n--- 음료 구매 ---")
        drink = input("구매할 음료를 입력하세요 (콜라 / 사이다 / 환타): ")

        if drink in stock:
            quantity = int(input("구매할 수량을 입력하세요: "))

            if stock[drink] >= quantity:
                total_price = price[drink] * quantity
                stock[drink] -= quantity
                sales[drink] += total_price
                print(f"\n ✅ {drink} {quantity}개 구매 완료! 총 금액: {total_price}원")

            else:
                print(" ❌ 재고가 부족합니다.")
        else:
            print(" ❌ 취급하지 않는 음료입니다.")

    # ------------------------------
    # 2️⃣ 재고 및 매출 현황
    # ------------------------------

    # gpt로 이쁘게 꾸며봄
    elif choice == '2' :
        print("\n🥤 재고 현황 (현재)")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{'음료명':<8}{'재고':<6}{'가격':<6}{'매출':<10}")
        print("───────────────────────────────────────")

        for drink in stock:
            ICON = "🧊" if stock[drink] > 0 else "❌"
            name = align_korean(drink, 10)  # 한글 폭 고려
            print(f"{name}{ICON} {stock[drink]:<6}{price[drink]:<10}{sales[drink]:<10}")

        print("───────────────────────────────────────")
        print(f"💰 총 매출: {sum(sales.values())}원")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # ------------------------------
    # 3️⃣ 재고 관리
    # ------------------------------

    elif choice == '3':
        print("\n---재고 관리 (추가/삭제)---")
        commend = input("진행할 작업을 입력하세요: ")

        if commend == '추가':
            drink = input("추가할 음료를 입력하세요 (콜라 / 사이다 / 환타): ")
            quantity = int(input("추가할 수량을 입력하세요: "))

            if drink in stock:
                stock[drink] += quantity
            else:
                stock[drink] = quantity
                price[drink] = int(input("새로운 음료의 금액을 입력하세요: "))
                sales[drink] = 0
            print(f"\n ✅ {drink} {quantity}개 추가 완료 되었습니다.")

        elif commend == '삭제':
            drink = input("삭제할 음료를 입력하세요: ")

            if drink in stock:
                del stock[drink]
                del price[drink]
                del sales[drink]
                print(f'\n {drink} 삭제 완료.')

            else:
                print("\n ❌ 해당 음료가 존재하지 않습니다.")

        else:
            print("\n ❌ 실행할 수 없는 명령입니다.")

        print("\n🥤 재고 현황 (현재)")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{'음료명':<8}{'재고':<6}{'가격':<6}{'매출':<10}")
        print("───────────────────────────────────────")

        for drink in stock:
            ICON = "🧊" if stock[drink] > 0 else "❌"
            name = align_korean(drink, 10)  # 한글 폭 고려
            print(f"{name}{ICON} {stock[drink]:<6}{price[drink]:<10}{sales[drink]:<10}")

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # ------------------------------
    # 4️⃣ 프로그램 종료
    # ------------------------------

    elif choice == '4':
        print("\n--- 프로그램 종료 ---")
        break

    else:
        print("\n ❌ 실행할 수 없는 명령입니다.")

# ==============================
# 🔹 프로그램 종료 시 저장
# ==============================
data = {'stock': stock, 'price': price, 'sales': sales}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("\n💾 데이터 저장 완료!")
print("📊 최종 매출:", sum(sales.values()), "원")
print("👋 프로그램을 종료합니다.")
