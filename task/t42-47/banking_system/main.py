'''
    사용자로부터 입력을 받아 사용자를 추가하거나 찾고, 사용자 메뉴를 통해 입금, 출금, 잔고 확인, 거래 내역 기능을 제공하는 메인 함수를 구현합니다.
    실행 구문 : python3 -m banking_system.main
'''
import os
import sys

# 현재 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from banking_system.service.banking_service import BankingService
from banking_system.utils.exceptions import InsufficientFundsError, NegativeAmountError, UserNotFoundError

def main() -> None:
    ''' main 함수 '''
    system = BankingService()
    print("🏦 은행 시스템에 오신 것을 환영합니다!")
    print("=" * 50)

    while True:
        try:
            print("\n📋 메인 메뉴")
            print("1️⃣  사용자 추가")
            print("2️⃣  사용자 정보 조회")
            print("3️⃣  사용자 메뉴")
            print("4️⃣  전체 사용자 목록")
            print("5️⃣  사용자 검색")
            print("6️⃣  프로그램 종료")
            mode = int(input("\n원하는 모드를 선택해주세요 (1-6): "))

            if mode == 1:
                username = input("사용자 이름을 입력하세요. : ")
                system.add_user(username)
            elif mode == 2:
                username = input("조회할 사용자 이름을 입력하세요: ")
                system.show_user_info(username)
            elif mode == 3:
                username = input("사용자 이름을 입력하세요: ")
                system.user_menu(username)
            elif mode == 4:
                system.show_all_users()
            elif mode == 5:
                keyword = input("검색할 키워드를 입력하세요: ")
                system.search_users(keyword)
            elif mode == 6:
                print("👋 은행 시스템을 종료합니다. 이용해주셔서 감사합니다!")
                break
            else:
                print("❌ 1-6 중에서 선택해주세요.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")
        except InsufficientFundsError as e:
            print(f"❌ {e}")
        except NegativeAmountError as e:
            print(f"❌ {e}")
        except UserNotFoundError as e:
            print(f"❌ {e}")

# 이 파일이 직접 실행될 때만 아래 코드를 실행하고, 다른 파일에서 import될 때는 실행하지 않도록 함.
if __name__ == "__main__":
    main()
