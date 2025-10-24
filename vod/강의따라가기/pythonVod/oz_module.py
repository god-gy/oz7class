"""
41강 실습 파일
"""

#oz_module.py
PI = 3.141592

#반지름 값을 받아오는 함수
def number_input():
    value = input("반지름을 입력해주세요")
    return float(value)

#원의 둘레
def get_circum(radius):
    return 2 * PI * radius

#원의 넓이
def get_circle(radius):
    return PI * radius * radius
