from tkinter import Tk
class Window(Tk):
    def __init__(self):
        super().__init__()


        self.title("user mangment Application")

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.geometry("500x400")

    def show_form(self):
        self.mainloop()
