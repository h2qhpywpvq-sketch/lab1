#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5



# TODO здесь заполнение слова
def get_distance():
    distances = dict()
    for i in sites.keys():
        distances[i] = dict()
        for j in sites.keys():
            if (i!= j):
                t1 = sites[i]
                t2 = sites[j]
                distances[i][j] = ((t1[0] - t2[0]) ** 2 + (t1[1] - t2[0]) ** 2) ** 0.5
            
    print(distances)
    



get_distance()