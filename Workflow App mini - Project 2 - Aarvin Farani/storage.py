import csv
import os

class Storage:

    def __init__(self, file_name):
        self.file_name = file_name

    def save_tasks(self, tasks):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'importance', 'status'])
            writer.writeheader()
            writer.writerows(tasks)

    def load_tasks(self):
        tasks = []
        if not os.path.exists(self.file_name):
            return tasks
        with open(self.file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'].strip() != '':
                    tasks.append({
                        'name': row['name'],
                        'importance': row['importance'],
                        'status': row['status']
                    })
        return tasks
