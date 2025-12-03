"""Задание 9: множества цветов в саду и на лугу"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "garden"
    number = 9

    def run(self, *args, **kwargs):
        garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
        meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
        garden_set = set(garden)
        meadow_set = set(meadow)
        all_flowers = garden_set | meadow_set
        both = garden_set & meadow_set
        garden_only = garden_set - meadow_set
        meadow_only = meadow_set - garden_set
        return f"все:{sorted(all_flowers)}; оба:{sorted(both)}; только_в_саду:{sorted(garden_only)}; только_на_лугу:{sorted(meadow_only)}"
