"""Задание 2: площадь круга и принадлежность точки"""
from lab1.main import TaskBase
import math


class Task(TaskBase):
    name = "circle"
    number = 2

    def get_area_circle(self, radius: float) -> float:
        return round(3.1415926 * radius ** 2, 4)

    def is_point_in_circle(self, point, radius: float) -> bool:
        return (point[0] ** 2 + point[1] ** 2) ** 0.5 <= radius

    def run(self, *args, **kwargs):
        radius = 42
        point_1 = (23, 34)
        point_2 = (30, 30)
        area = self.get_area_circle(radius)
        return f"area={area}; p1_in={self.is_point_in_circle(point_1, radius)}; p2_in={self.is_point_in_circle(point_2, radius)}"
