class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, name, importance):
        name = name.strip()
        if name == '':
            return False
        task = {'name': name, 'importance': importance, 'status': 'Not Done'}
        self.tasks.append(task)
        return True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['status'] = 'Done'

    def get_tasks(self):
        return self.tasks

    def set_tasks(self, tasks):
        self.tasks = tasks
