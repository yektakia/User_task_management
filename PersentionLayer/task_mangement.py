import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
from tkinter.ttk import Treeview
from BusinesslogicLayer.user_business_logic import UserBusinessLogic
class Taskmanagement(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.current_user = None
        self.item_list = []
        self.main_view = main_view
        self.current_user = None
        self.user_businesslogic = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.header = Label(self, text="Task Management Form")
        self.header.grid(row=0, column=0, pady=10, padx=10)

        self.add_task_button = Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.remove_task_button = Button(self, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=1, column=0, pady=(0, 10), padx=10)

        self.edit_task_button = Button(self, text="Edit Task", command=self.edit_task)
        self.edit_task_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.task_table = Treeview(self, columns=("task", "status"))
        self.task_table.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="nsew")

        self.task_table.heading("#0", text="No")
        self.task_table.heading("#1", text="task")
        self.task_table.heading("#2", text="status")

    def set_current_user(self, current_user):
        response = self.user_businesslogic.get_tasks(current_user)
        if response.success:
            self.load_data(response.data)
        else:
            messagebox.showerror("Error", response.message)

    def load_data(self, task_list):
        for item in self.item_list:
            self.task_table.delete(item)
        self.item_list.clear()

        row_number = 1
        for task in task_list:
            item = self.task_table.insert("", "end", iid=task.id, text=row_number,
                                          values=(task.name, task.status))
            self.item_list.append(item)
            row_number += 1

    def add_task(self):
        self.main_view.switch_frame("add_task")
        self.set_current_user(self.current_user)

    def remove_task(self):
        selected_items = self.task_table.selection()
        self.user_businesslogic.remove_task(selected_items)
        self.set_current_user(self.current_user)
        messagebox.showinfo("Success", "Task Deleted")

    def edit_task(self):
        selected_items = self.task_table.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a task to edit.")
            return

        item_id = selected_items[0]
        task_name, task_status = self.task_table.item(item_id, 'values')

        edit_frame = self.main_view.switch_frame("edit_task")
        edit_frame.load_task_details(task_name, task_status, item_id)


class Add_task(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.current_user = None
        self.main_view = main_view
        self.user_businesslogic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)
        self.header = Label(self, text="Add task Form")
        self.header.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        self.task_label = Label(self, text="Task")
        self.task_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.task_entry = Entry(self)
        self.task_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.submit_button = Button(self, text="Add", command=self.submit)
        self.submit_button.grid(row=3, column=1, pady=(0, 10), padx=0, sticky="w")

    def submit(self):
        new_task = self.task_entry.get()
        if not new_task:
            messagebox.showwarning("Warning", "Task cannot be empty.")
            return

        response = self.user_businesslogic.add_task(new_task)
        if response.success:
            messagebox.showinfo("Success", "Task added successfully.")
            second_response = self.user_businesslogic.get_tasks(self.current_user)
            task_mangement_frame = self.main_view.switch_frame("task_management")
            task_mangement_frame.load_data(second_response.data)

        else:
            messagebox.showerror("Error", response.message)


class Edit_task(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.current_user = None
        self.main_view = main_view
        self.user_businesslogic = UserBusinessLogic()
        self.task_id = None

        self.grid_columnconfigure(1, weight=1)
        self.header = Label(self, text="Edit Task Form")
        self.header.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        self.task_name_label = Label(self, text="Task Name")
        self.task_name_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.task_status_label = Label(self, text="Task Status")
        self.task_status_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.task_name_entry = Entry(self)
        self.task_name_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.task_status_entry = Entry(self)
        self.task_status_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.submit_button = Button(self, text="Update", command=self.submit)
        self.submit_button.grid(row=3, column=1, pady=(0, 10), padx=0, sticky="w")

    def load_task_details(self, task_name, task_status, task_id):
        self.task_name_entry.delete(0, tk.END)
        self.task_name_entry.insert(0, task_name)
        self.task_status_entry.delete(0, tk.END)
        self.task_status_entry.insert(0, task_status)
        self.task_id = task_id
    def submit(self):
        new_task_name = self.task_name_entry.get()
        new_task_status = self.task_status_entry.get()

        if not new_task_name or not new_task_status:
            messagebox.showwarning("Warning", "Task name and status cannot be empty.")
            return

        response = self.user_businesslogic.edit_task(self.task_id, new_task_name, new_task_status)
        if response.success:
            messagebox.showinfo("Success", "Task updated successfully.")
            second_response = self.user_businesslogic.get_tasks(self.current_user)
            task_management_frame = self.main_view.switch_frame("task_management")
            task_management_frame.load_data(second_response.data)
        else:
            messagebox.showerror("Error", response.message)