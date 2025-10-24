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
        print(f"✅ {username} 사용자가 추가되었습니다.")

    def find_user(self, username:str) -> User:
        '''사용자찾기'''
        for user in self.user:
            if username == user.username:
                print(f"✅ {username} 사용자를 찾았습니다.")
                return user
        return None

    def show_user_info(self, username: str) -> None:
        '''사용자 상세 정보 표시'''
        user = self.find_user(username)
        if user is None:
            print(f"❌ {username} 사용자를 찾을 수 없습니다.")
            return

        print(f"\n👤 {username}님의 계좌 정보")
        print("=" * 40)
        print(f"💰 현재 잔고: {user.account.get_balance():,}원")

        transactions = user.account.get_transaction()
        print(f"📊 총 거래 횟수: {len(transactions)}회")

        if transactions:
            # 입금/출금 통계
            deposits = [t for t in transactions if t.transaction_type == "입금"]
            withdrawals = [t for t in transactions if t.transaction_type == "출금"]

            total_deposits = sum(t.amount for t in deposits)
            total_withdrawals = sum(t.amount for t in withdrawals)

            print(f"📈 총 입금액: {total_deposits:,}원 ({len(deposits)}회)")
            print(f"📉 총 출금액: {total_withdrawals:,}원 ({len(withdrawals)}회)")

            # 최근 거래 내역 (최대 3개)
            # print(f"\n📋 최근 거래 내역 (최대 3개)")
            print("-" * 30)
            recent_transactions = transactions[-3:] if len(transactions) >= 3 else transactions
            for i, transaction in enumerate(reversed(recent_transactions), 1):
                print(f"{i}. {transaction}")
        else:
            print("📋 거래 내역이 없습니다.")

        print("=" * 40)

    def show_all_users(self) -> None:
        '''전체 사용자 목록 표시'''
        if not self.user:
            print("📋 등록된 사용자가 없습니다.")
            return

        print(f"\n👥 전체 사용자 목록 (총 {len(self.user)}명)")
        print("=" * 50)
        for i, user in enumerate(self.user, 1):
            balance = user.account.get_balance()
            transaction_count = len(user.account.get_transaction())
            print(f"{i:2d}. {user.username:<15} | 잔고: {balance:>8,}원 | 거래: {transaction_count:>2}회")
        print("=" * 50)

    def search_users(self, keyword: str) -> None:
        '''사용자 검색 (부분 일치)'''
        matching_users = [user for user in self.user if keyword.lower() in user.username.lower()]

        if not matching_users:
            print(f"🔍 '{keyword}'와 일치하는 사용자가 없습니다.")
            return

        print(f"\n🔍 '{keyword}' 검색 결과 ({len(matching_users)}명)")
        print("=" * 50)
        for i, user in enumerate(matching_users, 1):
            balance = user.account.get_balance()
            transaction_count = len(user.account.get_transaction())
            print(f"{i:2d}. {user.username:<15} | 잔고: {balance:>8,}원 | 거래: {transaction_count:>2}회")
        print("=" * 50)

    def user_menu(self, username:str) -> None:
        '''사용자 메뉴 제공. 모드선택'''
        user = self.find_user(username)

        if user is None:
            print(f"{username} 사용자를 찾을 수 없습니다.")
            return

        print(f"\n👤 {username}님의 계좌 메뉴")
        print("=" * 30)

        while True:
            try:
                print("\n💳 계좌 메뉴")
                print("💰 입금")
                print("💸 출금")
                print("📊 잔고확인")
                print("📋 거래내역")
                print("🚪 종료")
                mode = input("\n원하는 기능을 선택하세요: ")
                if mode == '종료':
                    print("계좌 메뉴를 종료합니다.")
                    break
                elif mode == '입금':
                    amount = int(input("입금할 금액을 입력하세요: "))
                    user.account.deposit(amount)
                    print(f"✅ {amount:,}원이 입금되었습니다. 현재 잔고: {user.account.get_balance():,}원")
                elif mode == '출금':
                    amount = int(input("출금할 금액을 입력하세요: "))
                    user.account.withdraw(amount)
                    print(f"✅ {amount:,}원이 출금되었습니다. 현재 잔고: {user.account.get_balance():,}원")
                elif mode == '잔고확인':
                    print(f'💰 현재 잔고: {user.account.get_balance():,}원')
                elif mode == '거래내역':
                    transactions = user.account.get_transaction()
                    if transactions:
                        print('\n📋 거래내역')
                        print("-" * 40)
                        for i, transaction in enumerate(transactions, 1):
                            print(f"{i:2d}. {transaction}")
                        print("-" * 40)
                    else:
                        print('📋 거래내역이 없습니다.')
            except ValueError:
                print('안내드린 모드 안에서 작성해 주세요.')
