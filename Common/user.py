class User:
    def __init__(self, id, first_name, last_name, username, password, active, role_id, task_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.active = True if active == 1 else False
        self.role_id = role_id
        self.task_id = task_id

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def is_admin(self):
        return self.role_id == 1
