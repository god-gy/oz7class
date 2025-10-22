'''
    main
'''
import os
import sys
from banking_system.service.banking_service import BankingService
from banking_system.utils.exceptions import InsufficientFundsError, NegativeAmountError, UserNotFoundError

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main() -> None:
    ''' main 함수 '''
    system = BankingService()

    while True:
        try:
            mode = int(input("원하는 모드를 선택해주세요. (1:사용자추가 2:사용자찾기 3:프로그램종료): "))

            if mode == 3:
                break
            elif mode == 1:
                username = input("사용자 이름을 입력하세요. : ")
                system.add_user(username)
            elif mode == 2:
                username = input("사용자 이름을 입력하세요. : ")
                system.find_user(username)
            else:
                print("주어진 보기 중 선택하세요.")
        except ValueError as e:
            print(e)
        except InsufficientFundsError as e:
            print(e)
        except NegativeAmountError as e:
            print(e)
        except UserNotFoundError as e:
            print(e)

# 이 파일이 직접 실행될 때만 아래 코드를 실행하고, 다른 파일에서 import될 때는 실행하지 않도록 함.
if __name__ == "__main__":
    main()
