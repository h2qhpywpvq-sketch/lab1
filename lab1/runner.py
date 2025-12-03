"""Верхнеуровневый раннер: использует `TaskRegistry` из `lab1.main`.

Предоставляет `run_all()` и `cli()` для запуска всех задач.
"""
from lab1.main import TaskRegistry


def run_all():
    reg = TaskRegistry()
    reg.load_tasks()
    return reg.run_all()


def cli():
    results = run_all()
    for num, out in sorted(results.items()):
        print(f"Задача {num}: {out}")


if __name__ == '__main__':
    cli()
