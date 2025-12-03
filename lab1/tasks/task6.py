"""Задание 6: операции со списком зоопарка"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "zoo"
    number = 6

    def run(self, *args, **kwargs):
        zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
        zoo.insert(1, 'bear')
        birds = ['rooster', 'ostrich', 'lark']
        zoo.extend(birds)
        if 'elephant' in zoo:
            zoo.remove('elephant')
        lion_pos = zoo.index('lion') + 1
        lark_pos = zoo.index('lark') + 1
        return f"{zoo}\nлев в клетке {lion_pos}\nжаворонок в клетке {lark_pos}"
