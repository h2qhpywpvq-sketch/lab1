from lab1.main import TaskRegistry


def test_task3_produces_25():
    reg = TaskRegistry()
    reg.load_tasks()
    results = reg.run_all()
    # task 3 should compute 25
    assert '25' in results[3]


def test_task11_contains_lamp_summary():
    reg = TaskRegistry()
    reg.load_tasks()
    results = reg.run_all()
    assert 'Лампа' in results[11]
