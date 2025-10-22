'''
    계좌를 나타내는 클래스입니다. 잔고와 거래 내역을 관리합니다.
    입금, 출금, 잔고 확인 및 거래 내역을 반환하는 메서드를 구현합니다.
    클래스 변수로 은행 이름을 관리하고, 이를 설정하고 반환하는 메서드를 구현합니다.
'''
from banking_system.models.transaction import Transaction
from banking_system.utils.decorators import validate_transaction
from banking_system.utils.exceptions import InsufficientFundsError
class Account:
    ''' 계좌 '''

    bank_name = "무슨은행"

    def __init__(self) -> None:
        '''잔고와 거래 내역을 초기화'''
        self.__balance = 0
        self.transaction = []

    @validate_transaction
    def deposit(self, amount:int) -> None:
        '''금액을 입금하고, 거래 내역에 추가'''
        self.__balance += amount
        self.transaction.append(Transaction("입금", amount, self.__balance))

    @validate_transaction
    def withdraw(self, amount:int) -> None:
        '''금액을 출금하고, 거래 내역에 추가'''
        if amount > self.__balance:
            raise InsufficientFundsError
        self.__balance -= amount
        self.transaction.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        '''현재 잔고를 반환'''
        return self.__balance

    def get_transaction(self) -> list:
        '''거래 내역을 반환'''
        return self.transaction

    @classmethod
    def get_bank_name(cls) -> str:
        '''은행 이름을 반환하는 클래스 메서드'''
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name:str) -> None:
        '''은행 이름을 설정하는 클래스 메서드'''
        cls.bank_name = name
