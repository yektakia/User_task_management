from DataAccessLayer.user_data_access import User_data_access
from Common.response import Response
from Common.user import User
from Common.Task import Task


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = User_data_access()

    def login(self, username, password):

        if len(username) < 3 or len(password) < 6:
            return Response(None, "Invalid data", False)
        user = self.user_data_access.get_user(username, password)
        if user:
            if user.active:
                return Response(user, "Successful", True)
            else:
                return Response(None, " your account is deactive", False)

        else:
            return Response(None, "Invalid user or pass", False)

    def get_users(self, current_user):
        if not current_user.is_admin():
            return Response(None, " Invalid access", False)
        if not current_user.active:
            return Response(None, " your account is deactive", False)

        user_list = self.user_data_access.get_users(current_user.id)

        return Response(user_list, "Successful", True)

    def active_users(self, ids):
        for id in ids:
            self.user_data_access.active_users(id, 1)

    def deactive_users(self, ids):
        for id in ids:
            self.user_data_access.active_users(id, 0)

    def register(self, first_name, last_name, username, password):

        if len(first_name) < 3 or len(last_name) < 3 or len(username) < 3 or len(password) < 6:
            return Response(None, "firstname,lastname,username and password should be longer", False)
        user = self.user_data_access.add_users(first_name, last_name, username, password)

        return Response(user, "sucessful", True)

    def update(self, first_name, last_name):

        if len(first_name) < 3 or len(last_name) < 3:
            return Response(None, "firstname,lastname,username and password should be longer", False)
        update_user = self.user_data_access.update_users(first_name, last_name)

        return Response(update_user, "sucessful", True)

    def add_admin(self, ids):
        for id in ids:
            self.user_data_access.add_admin(id, 1)

    def add_task(self, task_name):
        new_task = self.user_data_access.add_task(task_name)
        return Response(new_task, "sucessful", True)

    def get_tasks(self, current_user):
        task_list = self.user_data_access.get_tasks()
        return Response(task_list, "Successful", True)

    def remove_task(self, task_list):
        for item in task_list:
            tasks = self.user_data_access.remove_task(item)

    def edit_task(self, task_id, task_name, task_status):
        updated_task = self.user_data_access.edit_task(task_id, task_name, task_status)
        return Response(updated_task, "Successful", True)
