'''
    여러 사용자를 관리하는 서비스 클래스입니다.
    사용자를 추가하고, 찾고, 사용자 메뉴를 제공하는 메서드를 구현합니다.

    - users: 사용자 목록을 저장하는 리스트
    - username: 사용자의 이름을 나타내는 문자열
    - user: User 객체를 나타내는 변수
    - amount: 입금 또는 출금 금액을 나타내는 정수
    - choice: 사용자의 선택을 나타내는 문자열
'''
from banking_system.models.user import User
class BankingService:
    '''서비스'''
    def __init__(self) -> None:
        '''사용자 목록을 초기화'''
        self.user = []

    def add_user(self, username:str) -> None:
        '''사용자추가'''
        self.user.append(User(username))
        print("사용자 추가 완료")

    def find_user(self, username:str) -> User:
        '''사용자찾기'''
        for user in self.user:
            if username == self.user:
                print("사용자 찾기 완료")
                return user
        return None

    def user_menu(self, username:str) -> None:
        '''사용자 메뉴 제공. 모드선택'''
        user = self.find_user(username)

        while True:
            try:
                mode = input("희망하는 모드를 선택하세요 (입금, 출금, 잔고확인, 거래내역, 종료): ")
                if mode == '종료':
                    break
                elif mode == '입금':
                    amount = int(input("입금할 금액을 입력하세요: "))
                    user.account.deposit(amount)
                elif mode == '출금':
                    amount = int(input("출금할 금액을 입력하세요: "))
                    user.account.withdraw(amount)
                elif mode == '잔고확인':
                    print(f'잔고 : {user.account.get_balance()}원')
                elif mode == '거래내역':
                    print(f'거래내역: {user.account.get_transaction()}')
            except ValueError:
                print('안내드린 모드 안에서 작성해 주세요.')
