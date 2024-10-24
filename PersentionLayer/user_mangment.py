# from tkinter import Frame, Label, Button, messagebox
# from tkinter.ttk import Treeview
# from BusinesslogicLayer.user_business_logic import UserBusinessLogic
#
#
# class Usermangement(Frame):
#     def __init__(self, main_view, window):
#         super().__init__(window)
#
#         self.item_list = []
#         self.current_user = None
#
#         self.userBusinessLogic = UserBusinessLogic()
#         self.main_view = main_view
#
#         self.grid_columnconfigure(0, weight=1)
#         self.rowconfigure(2, weight=1)
#
#         self.header = Label(self, text="User mangement")
#         self.header.grid(row=0, column=0, pady=10, padx=10)
#
#         self.active_button = Button(self, text="Active", command=self.user_activation)
#         self.active_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")
#
#         self.deactive_button = Button(self, text="Deactive", command=self.user_dactivation)
#         self.deactive_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")
#
#         self.add_admin_button = Button(self, text="Add admin", command=self.add_admin)
#         self.add_admin_button.grid(row=1, column=0, pady=(0, 10), padx=10)
#
#         self.user_table = Treeview(self, columns=("firstname", "lastname", "username", "status"))
#         self.user_table.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="nsew")
#
#         self.user_table.heading("#0", text="No")
#         self.user_table.heading("#1", text="Firstname")
#         self.user_table.heading("#2", text="Lastname")
#         self.user_table.heading("#3", text="Username")
#         self.user_table.heading("#4", text="Status")
#
#     def set_current_user(self, current_user):
#         self.current_user = current_user
#         if self.current_user.is_admin():
#             response = user_list = self.userBusinessLogic.get_users(current_user)
#             if response.success:
#                 self.load_data(response.data)
#             else:
#                 messagebox.showerror("Error", response.message)
#
#     def load_data(self, user_list):
#         for items in self.item_list:
#             self.user_table.delete(items)
#
#         self.item_list.clear()
#         row_number = 1
#         for user in user_list:
#             item = self.user_table.insert("",
#                                           "end",
#                                           iid=user.id,
#                                           text=row_number,
#                                           values=(user.first_name, user.last_name, user.username,
#                                                   "Active" if user.active else "Deactive"))
#             self.item_list.append(item)
#             row_number += 1
#
#     def user_activation(self):
#         if self.current_user.is_admin():
#             user_ids = self.user_table.selection()
#             self.userBusinessLogic.active_users(user_ids)
#             response = user_list = self.userBusinessLogic.get_users(self.current_user)
#             self.load_data(response.data)
#
#     def user_dactivation(self):
#         if self.current_user.is_admin():
#             user_ids = self.user_table.selection()
#             self.userBusinessLogic.deactive_users(user_ids)
#             response = user_list = self.userBusinessLogic.get_users(self.current_user)
#             self.load_data(response.data)
#
#     def add_admin(self):
#         if self.current_user.is_admin():
#             user_ids = self.user_table.selection()
#             self.userBusinessLogic.add_admin(user_ids)
#             response = user_list = self.userBusinessLogic.get_users(self.current_user)
#             self.load_data(response.data)
from tkinter import Frame, Label, Button, messagebox
from tkinter.ttk import Treeview
from BusinesslogicLayer.user_business_logic import UserBusinessLogic


class UserManagement(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.item_list = []
        self.current_user = None

        self.userBusinessLogic = UserBusinessLogic()
        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.header = Label(self, text="User Management")
        self.header.grid(row=0, column=0, pady=10, padx=10)

        self.active_button = Button(self, text="Activate", command=self.user_activation)
        self.active_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.deactive_button = Button(self, text="Deactivate", command=self.user_deactivation)
        self.deactive_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.add_admin_button = Button(self, text="Add Admin", command=self.add_admin)
        self.add_admin_button.grid(row=1, column=0, pady=(0, 10), padx=10)

        self.user_table = Treeview(self, columns=("firstname", "lastname", "username", "status"), show='headings')
        self.user_table.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="nsew")

        self.user_table.heading("#1", text="Firstname")
        self.user_table.heading("#2", text="Lastname")
        self.user_table.heading("#3", text="Username")
        self.user_table.heading("#4", text="Status")

    def set_current_user(self, current_user):
        self.current_user = current_user
        if self.current_user.is_admin():
            response = self.userBusinessLogic.get_users(current_user)
            if response.success:
                self.load_data(response.data)
            else:
                messagebox.showerror("Error", response.message)

    def load_data(self, user_list):
        for item in self.item_list:
            self.user_table.delete(item)
        self.item_list.clear()

        row_number = 1
        for user in user_list:
            item = self.user_table.insert("", "end", iid=user.id, text=row_number,
                                          values=(user.first_name, user.last_name, user.username,
                                                  "Active" if user.active else "Deactivated"))
            self.item_list.append(item)
            row_number += 1

    def user_activation(self):
        if self.current_user.is_admin():
            user_ids = self.user_table.selection()
            if user_ids:
                for user_id in user_ids:
                    self.userBusinessLogic.active_users(user_id)  # Active a single user
                response = self.userBusinessLogic.get_users(self.current_user)
                self.load_data(response.data)

    def user_deactivation(self):
        if self.current_user.is_admin():
            user_ids = self.user_table.selection()
            if user_ids:
                for user_id in user_ids:
                    self.userBusinessLogic.deactive_users(user_id)  # Deactivate a single user
                response = self.userBusinessLogic.get_users(self.current_user)
                self.load_data(response.data)

    def add_admin(self):
        if self.current_user.is_admin():
            user_ids = self.user_table.selection()
            if user_ids:
                for user_id in user_ids:
                    self.userBusinessLogic.add_admin(user_id)  # Add admin for a single user
                response = self.userBusinessLogic.get_users(self.current_user)
                self.load_data(response.data)