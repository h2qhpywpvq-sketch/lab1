import importlib
import pkgutil
import inspect
from typing import Dict, Type

class TaskBase:
	"""
	Базовый интерфейс для всех задач.
	Каждый модуль lab1.tasks.taskN должен экспортировать класс Task(TaskBase).
	"""
	name: str = "base"
	number: int = 0

	def run(self, *args, **kwargs):
		raise NotImplementedError


class TaskRegistry:
	"""
	Загружает все модули в пакете lab1.tasks и собирает классы, унаследованные от TaskBase.
	"""
	def __init__(self):
		self.tasks: Dict[int, Type[TaskBase]] = {}

	def load_tasks(self):
		import lab1.tasks as tasks_pkg
		pkgpath = tasks_pkg.__path__
		for finder, name, ispkg in pkgutil.iter_modules(pkgpath):
			modname = f"lab1.tasks.{name}"
			mod = importlib.import_module(modname)
			# Найти класс-наследник TaskBase
			for _, obj in inspect.getmembers(mod, inspect.isclass):
				if issubclass(obj, TaskBase) and obj is not TaskBase:
					inst = obj()
					self.tasks[getattr(inst, "number", len(self.tasks)+1)] = obj
		return self.tasks

	def run_all(self):
		results = {}
		for num, cls in sorted(self.tasks.items()):
			instance = cls()
			results[num] = instance.run()
		return results


def discover_and_run_all():
	reg = TaskRegistry()
	reg.load_tasks()
	return reg.run_all()