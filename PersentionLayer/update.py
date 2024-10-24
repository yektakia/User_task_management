from tkinter import Frame, Label, Entry, Button, messagebox
from BusinesslogicLayer.user_business_logic import UserBusinessLogic


class Update(Frame):
    def __init__(self, main_view, window):
        super().__init__(window)
        self.main_view = main_view
        self.businesslogic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)
        self.header = Label(self, text="Update Form")
        self.header.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        self.firstname_label = Label(self, text="Firstname")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Lastname")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.update_button = Button(self, text="submit", command=self.update)
        self.update_button.grid(row=3, column=1, pady=(0, 10), padx=0, sticky="w")

    def update(self):
        update_first_name = self.firstname_entry.get()
        update_last_name = self.lastname_entry.get()
        respone_upadte_user = self.businesslogic.update(update_first_name, update_last_name)

        if not respone_upadte_user.success:
            messagebox.showerror("Error", respone_upadte_user.message)
        else:
            self.clear_data()
            home_frame = self.main_view.switch_frame("home")
            home_frame.set_current_user(respone_upadte_user.data)

    def clear_data(self):
        self.firstname_entry.delete(0, "end")
        self.lastname_entry.delete(0, "end")


