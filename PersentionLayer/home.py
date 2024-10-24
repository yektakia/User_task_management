from tkinter import Frame, Label, Button


class HomeFrame(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)

        self.current_user = None
        self.main_view = main_view
        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="")
        self.header.grid(row=0, column=0, pady=10, padx=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.update_button = Button(self, text="Update", command=self.update)
        self.update_button.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.update_button = Button(self, text="Task Mangement", command=self.go_task_management)
        self.update_button.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="ew")
    def set_current_user(self, current_user):
        self.current_user = current_user
        self.header.config(text=f"Welcome {current_user.get_fullname()}")
        if current_user.is_admin():
            self.user_mangment_button = Button(self, text="User mangment", command=self.go_user_mangment)
            self.user_mangment_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="ew")

    def logout(self):
        self.main_view.switch_frame("login")

    def go_user_mangment(self):
        if self.current_user.is_admin():
            user_mangement_frame = self.main_view.switch_frame("user_mangement")
            user_mangement_frame.set_current_user(self.current_user)

    def update(self):
        self.main_view.switch_frame("update")

    def go_task_management(self):
        task_management_frame = self.main_view.switch_frame("task_management")
        task_management_frame.set_current_user(self.current_user)

