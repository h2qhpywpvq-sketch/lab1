# Лабораторная работа 1 — набор заданий

В этом репозитории реализовано 11 заданий на Python как модули в `lab1/tasks`.

Структура:

- `lab1/tasks/task1.py` ... `task11.py` — модули задач с классами `Task(TaskBase)`.
- `lab1/main.py` — обнаружение задач и `TaskRegistry`.
- `lab1/runner.py` — верхнеуровневый раннер для запуска задач.
- `tests/` — тесты на `pytest`.
- `report.md` — шаблон отчёта.

Python: совместимо с Python 3.8/3.9 и выше.

Запуск тестов:

```bash
python3 -m pip install -r requirements.txt
pytest -q
```

Запуск всех задач:

```bash
python -m lab1.runner
```
# Лабораторная работа — структура репозитория

Инструкции:
- Установите Python 3.8/3.9.
- Создайте virtualenv:
  python3 -m venv .venv
  source .venv/bin/activate
- Установите зависимости:
  pip install -r requirements.txt
- Сгенерируйте шаблоны задач (если нужно):
  python3 scripts/create_tasks.py
- Реализуйте решения задач в lab1/tasks/task1.py … task11.py, соблюдая интерфейс TaskBase.
- Запустите тесты:
  pytest -q

Структура:
- lab1/ — пакет с основным модулем и подпакетом tasks
- lab1/tasks/ — модули задач (task1..task11)
- scripts/create_tasks.py — генератор шаблонов задач
- tests/ — pytest тесты
- report.md — шаблон отчёта
