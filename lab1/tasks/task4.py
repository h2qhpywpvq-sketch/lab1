"""Задание 4: выделение фильмов из строки"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "favorite_movies"
    number = 4

    def run(self, *args, **kwargs):
        my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
        parts = [p.strip() for p in my_favorite_movies.split(',')]
        # первый, последний, второй, второй с конца
        out = f"{parts[0]}\n{parts[-1]}\n{parts[1]}\n{parts[-2]}"
        return out
