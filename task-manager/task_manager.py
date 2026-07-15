# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append({'name': name, 'done': False})
        print(f'任务 {name} 已添加')

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = '✓' if task['done'] else '○'
            print(f'{i}. [{status}] {task["name"]}')
