"""
mymath.py - 수학적 연산을 수행하는 모듈
"""

import math

def triangle_area(base, height):
    """
    삼각형의 넓이를 계산합니다.
    
    Args:
        base (float): 밑변 길이
        height (float): 높이
    
    Returns:
        float: 삼각형의 넓이
    """
    return (base * height) / 2

def circle_area(radius):
    """
    원의 넓이를 계산합니다.
    
    Args:
        radius (float): 반지름
    
    Returns:
        float: 원의 넓이
    """
    return math.pi * radius ** 2

def rectangular_prism_surface_area(length, width, height):
    """
    직육면체의 표면적을 계산합니다.
    
    Args:
        length (float): 길이
        width (float): 너비
        height (float): 높이
    
    Returns:
        float: 직육면체의 표면적
    """
    return 2 * (length * width + length * height + width * height)
