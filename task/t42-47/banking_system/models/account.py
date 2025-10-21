'''
계좌를 나타내는 클래스입니다. 잔고와 거래 내역을 관리합니다.
입금, 출금, 잔고 확인 및 거래 내역을 반환하는 메서드를 구현합니다.
클래스 변수로 은행 이름을 관리하고, 이를 설정하고 반환하는 메서드를 구현합니다.
'''

class Account:

    bank_name = "무슨은행"

    def __init__(self) -> None:
        self.__balance = 0
        self.transaction = []

    def deposit(self, amount:int) -> None:
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount:int) -> None:
        if 0 < amount < self.__balance:
            self.__balance += amount + self.__balance
        
    def get_balance(self) -> int:
        return self.__balance
    
    def get_transaction(self) -> list:
        return self.transaction

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name:str) -> None:
        cls.bank_name = name
