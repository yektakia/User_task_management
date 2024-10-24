from PersentionLayer.window import Window
from PersentionLayer.login import LoginFrame
from PersentionLayer.home import HomeFrame
from PersentionLayer.user_mangment import UserManagement
from PersentionLayer.register import Register
from PersentionLayer.update import Update
from PersentionLayer.task_mangement import Taskmanagement, Add_task, Edit_task


class MainView:
    def __init__(self):
        self.frames = {}
        window = Window()

        self.add_frame("edit_task", Edit_task(self, window))
        self.add_frame("add_task", Add_task(self, window))
        self.add_frame("task_management", Taskmanagement(self, window))
        self.add_frame("update", Update(self, window))
        self.add_frame("user_mangement", UserManagement(self, window))
        self.add_frame("home", HomeFrame(self, window))
        self.add_frame("login", LoginFrame(self, window))
        self.add_frame("register", Register(self, window))
        window.show_form()

    def add_frame(self, name, frame):
        self.frames[name] = frame
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        return frame
