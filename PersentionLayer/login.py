from tkinter import Frame, Label, Entry, Button, messagebox,END
from BusinesslogicLayer.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)
        self.main_view = main_view
        self.user_businesslogic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)
        self.header = Label(self, text="Login Form")
        self.header.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self)
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), padx=0, sticky="w")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = self.user_businesslogic.login(username, password)
        if not response.success:
            messagebox.showerror("Error", response.message)
        else:
            self.clear_data()
            home_frame = self.main_view.switch_frame("home")
            home_frame.set_current_user(response.data)

    def clear_data(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
