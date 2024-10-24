from tkinter import Frame, Label, Entry, Button, messagebox
from BusinesslogicLayer.user_business_logic import UserBusinessLogic


class Register(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)
        self.main_view = main_view
        self.user_businesslogic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)
        self.header = Label(self, text="Register Form")
        self.header.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        self.firstname_label = Label(self, text="Firstname")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Lastname")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self)
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.register_button = Button(self, text="register", command=self.register)
        self.register_button.grid(row=5, column=1, pady=(0, 10), padx=0, sticky="w")

    def register(self):
        first_name = self.firstname_entry.get()
        last_name = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = self.user_businesslogic.register(first_name, last_name, username, password)

        if not response.success:
            messagebox.showerror("Error", response.message)
        else:
            login_frame = self.main_view.switch_frame("login")
            return login_frame
