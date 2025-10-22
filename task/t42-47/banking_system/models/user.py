'''
    사용자를 나타내는 클래스입니다. 사용자 이름과 계좌를 속성으로 가지고 있습니다.
    생성자를 통해 사용자 이름과 계좌를 초기화합니다.

    username: 사용자의 이름을 나타내는 문자열
    account: 사용자의 계좌를 나타내는 Account 객체
'''

from banking_system.models.account import Account

class User:
    '''사용자 이름과 계좌를 초기화'''
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account()
