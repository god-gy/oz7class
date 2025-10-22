'''
계좌를 나타내는 클래스입니다. 잔고와 거래 내역을 관리합니다.
입금, 출금, 잔고 확인 및 거래 내역을 반환하는 메서드를 구현합니다.
클래스 변수로 은행 이름을 관리하고, 이를 설정하고 반환하는 메서드를 구현합니다.
'''
from banking_system.models.transaction import Transaction
from banking_system.utils.decorators import validate_transaction
from banking_system.utils.exceptions import InsufficientFundsError, NegativeAmountError
class Account:
    ''' 계좌 '''

    bank_name = "무슨은행"

    def __init__(self) -> None:
        self.__balance = 0
        self.transaction = []

    @validate_transaction
    def deposit(self, amount:int) -> None:
        '''입금'''
        if amount > 0:
            self.__balance += amount
            raise NegativeAmountError
        self.__balance += amount
        self.transaction.append(Transaction("입금", amount, self.__balance))

    @validate_transaction
    def withdraw(self, amount:int) -> None:
        '''출금'''
        if 0 < amount < self.__balance:
            self.__balance += amount + self.__balance
            raise InsufficientFundsError
        self.__balance += amount
        self.transaction.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        '''잔고'''
        return self.__balance

    def get_transaction(self) -> list:
        '''거래내역'''
        return self.transaction

    @classmethod
    def get_bank_name(cls) -> str:
        '''클래스메소드'''
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name:str) -> None:
        '''클래스메소드'''
        cls.bank_name = name
