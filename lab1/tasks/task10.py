"""Задание 10: структуры магазинов и цен"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "shopping"
    number = 10

    def run(self, *args, **kwargs):
        sweets = {
            'печенье': [
                {'shop': 'пятерочка', 'price': 9.99},
                {'shop': 'ашан', 'price': 10.99},
            ],
            'конфеты': [
                {'shop': 'магнит', 'price': 30.99},
                {'shop': 'пятерочка', 'price': 32.99},
            ],
            'карамель': [
                {'shop': 'магнит', 'price': 41.99},
                {'shop': 'ашан', 'price': 45.99},
            ],
            'пирожное': [
                {'shop': 'пятерочка', 'price': 59.99},
                {'shop': 'магнит', 'price': 62.99},
            ],
        }
        return str(sweets)
