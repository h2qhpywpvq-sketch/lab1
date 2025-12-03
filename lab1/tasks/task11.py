"""Задание 11: расчёт стоимости товаров на складе"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "store"
    number = 11

    def run(self, *args, **kwargs):
        goods = {
            'Лампа': '12345',
            'Стол': '23456',
            'Диван': '34567',
            'Стул': '45678',
        }
        store = {
            '12345': [
                {'quantity': 27, 'price': 42},
            ],
            '23456': [
                {'quantity': 22, 'price': 510},
                {'quantity': 32, 'price': 520},
            ],
            '34567': [
                {'quantity': 2, 'price': 1200},
                {'quantity': 1, 'price': 1150},
            ],
            '45678': [
                {'quantity': 50, 'price': 100},
                {'quantity': 12, 'price': 95},
                {'quantity': 43, 'price': 97},
            ],
        }
        lines = []
        for item_name, code in goods.items():
            entries = store[code]
            total_q = sum(e['quantity'] for e in entries)
            total_cost = sum(e['quantity'] * e['price'] for e in entries)
            lines.append(f"{item_name} - {total_q} шт, стоимость {total_cost} руб")
        return "\n".join(lines)
