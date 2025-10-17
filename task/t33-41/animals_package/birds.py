"""
birds 모듈
"""

class Eagle:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name}가 날아오릅니다: 🦅!"
