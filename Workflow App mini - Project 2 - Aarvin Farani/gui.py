import tkinter as tk
from tkinter import messagebox
from storage import Storage
from task_manager import TaskManager

class CheckingApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Checking Workflow App')
        self.geometry('500x430')
        self.resizable(False, False)

        self.manager = TaskManager()
        self.storage = Storage('tasks.csv')
        self.manager.set_tasks(self.storage.load_tasks())

        self.task_entry = tk.Entry(self, width=42)
        self.task_entry.pack(pady=15)

        self.importance_value = tk.StringVar(self)
        self.importance_value.set('Medium')
        self.importance_menu = tk.OptionMenu(self, self.importance_value, 'High', 'Medium', 'Low')
        self.importance_menu.config(width=15)
        self.importance_menu.pack(pady=5)

        self.add_button = tk.Button(self, text='Add Task', width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self, width=60, height=12)
        self.task_listbox.pack(pady=10)

        self.done_button = tk.Button(self, text='Mark Selected Done', width=20, command=self.mark_task_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(self, text='Delete Selected', width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.status_label = tk.Label(self, text='')
        self.status_label.pack(pady=5)

        self.refresh_list()
        self.protocol('WM_DELETE_WINDOW', self.close_app)

    def add_task(self):
        task_name = self.task_entry.get()
        importance = self.importance_value.get()

        if self.manager.add_task(task_name, importance):
            self.storage.save_tasks(self.manager.get_tasks())
            self.task_entry.delete(0, tk.END)
            self.importance_value.set('Medium')
            self.refresh_list()
            self.status_label.config(text='Task added')
        else:
            messagebox.showerror('Input Error', 'Please enter a task name.')

    def delete_task(self):
        index = self.get_selected_index()
        if index is None:
            messagebox.showerror('Selection Error', 'Please select a task to delete.')
            return

        self.manager.delete_task(index)
        self.storage.save_tasks(self.manager.get_tasks())
        self.refresh_list()
        self.status_label.config(text='Task deleted')

    def mark_task_done(self):
        index = self.get_selected_index()
        if index is None:
            messagebox.showerror('Selection Error', 'Please select a task to mark done.')
            return

        self.manager.mark_done(index)
        self.storage.save_tasks(self.manager.get_tasks())
        self.refresh_list()
        self.status_label.config(text='Task marked done')

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.manager.get_tasks():
            display = task['name'] + ' - ' + task['importance'] + ' - ' + task['status']
            self.task_listbox.insert(tk.END, display)

    def get_selected_index(self):
        selected = self.task_listbox.curselection()
        if not selected:
            return None
        return selected[0]

    def close_app(self):
        self.storage.save_tasks(self.manager.get_tasks())
        self.destroy()
