'''
    거래 내역을 나타내는 클래스입니다. 거래 유형, 금액, 잔고를 속성으로 가지고 있습니다.
    문자열로 거래 내역을 반환하는 메서드와 튜플로 반환하는 메서드를 구현합니다.
'''

class Transaction:
    ''' 거래내역 '''
    def __init__(self, transaction_type:str, amount:int, balance:int) -> None:
        '''거래 유형, 금액, 잔고를 초기화'''
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        '''거래 정보를 문자열로 반환'''
        return f'{self.transaction_type}: {self.amount}원, 잔액: {self.balance}'

    def to_tuple(self) -> tuple:
        ''' 거래 정보를 튜플로 반환'''
        return self.transaction_type, self.amount, self.balance
