"""Задание 3: операции, чтобы получить 25"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "operations"
    number = 3

    def run(self, *args, **kwargs):
        # один корректный пример, сохраняющий порядок 1 2 3 4 5 -> 25
        res = 1 * 2 + 3 + 4 * 5
        return str(res)
