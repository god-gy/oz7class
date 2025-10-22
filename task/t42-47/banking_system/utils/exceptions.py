'''
    오류처리
'''

class InsufficientFundsError(Exception):
    ''' 잔액부족시 '''
    def __init__(self, balance: int) -> None:
        super().__init__(f'잔액이 부족합니다. 현재 잔고 : {balance}원')

class NegativeAmountError(Exception):
    ''' 음수 입력시 '''
    def __init__(self) -> None:
        super().__init__('0보다 큰 금액만 가능합니다.')

class UserNotFoundError(Exception):
    ''' 사용자 확인 불가시 '''
    def __init__(self, username: str) -> None:
        super().__init__(f'{username} 사용자는 확인되지 않습니다.')
