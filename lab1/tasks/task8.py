"""Задание 8: расшифровка секретного сообщения"""
from lab1.main import TaskBase


class Task(TaskBase):
    name = "secret"
    number = 8

    def run(self, *args, **kwargs):
        secret_message = [
            'квевтфпп6щ3стмзалтнмаршгб5длгуча',
            'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
            'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
            'ьд5фму3ежородт9г686буиимыкучшсал',
            'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
        ]
        # декодирование по правилам задания
        w1 = secret_message[0][3]
        w2 = secret_message[1][9:13]
        w3 = secret_message[2][5:15:2]
        w4 = secret_message[3][12:6:-1]
        w5 = secret_message[4][20:15:-1]
        return f"{w1} {w2} {w3} {w4} {w5}"
