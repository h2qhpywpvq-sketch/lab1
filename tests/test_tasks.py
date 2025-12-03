from lab1.main import TaskRegistry


def test_load_all_tasks():
	# Проверяем, что реальная директория содержит 11 задач
	reg = TaskRegistry()
	tasks = reg.load_tasks()
	assert len(tasks) == 11

def test_run_all_returns_expected_strings():
	reg = TaskRegistry()
	reg.load_tasks()
	results = reg.run_all()
	for num, out in results.items():
		assert isinstance(out, str)
