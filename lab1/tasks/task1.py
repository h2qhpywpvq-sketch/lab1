"""Задание 1: расстояния между городами"""
from lab1.main import TaskBase

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


class Task(TaskBase):
    name = "distance"
    number = 1

    def run(self, *args, **kwargs):
        distances = {}
        for a, pa in sites.items():
            distances[a] = {}
            for b, pb in sites.items():
                if a == b:
                    distances[a][b] = 0.0
                else:
                    distances[a][b] = round(((pa[0]-pb[0])**2 + (pa[1]-pb[1])**2)**0.5, 3)
        return str(distances)
