'''
    데코레이터
'''

from typing import Callable
from functools import wraps  # 메타데이터 보존

def validate_transaction(func: Callable) -> Callable:
    @wraps(func)  # 원래 함수 정보 유지
    def wrapper(self, amount:int) -> None:
        if amount <= 0:
            raise ValueError('금액은 0보다 커야합니다.')
        return func(self, amount)
    return wrapper
