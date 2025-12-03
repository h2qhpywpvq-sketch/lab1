"""Задание 5: семья и рост"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "my_family"
    number = 5

    def run(self, *args, **kwargs):
        my_family_height = [
            ['отец', 180],
            ['мать', 165],
            ['сын', 175],
            ['дедушка', 170],
        ]
        father = my_family_height[0]
        total = sum(p[1] for p in my_family_height)
        return f"Рост отца - {father[1]} см\nОбщий рост моей семьи - {total} см"
