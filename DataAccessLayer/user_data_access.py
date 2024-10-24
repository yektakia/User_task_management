from Common.user import User
import sqlite3
from Common.Task import Task


class User_data_access:
    def __init__(self):
        self.database_name = "usermangement11.db"

    def get_user(self, username, password):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            data = curser.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   active,
                   role_id,
                   task_id
            FROM User
            Where username = ?
            And   password = ? """, [username, password]).fetchone()

            if data:
                user = User(data[0], data[1], data[2], data[3], None, data[5], data[6], data[7])
                return user

    def get_users(self, user_id):
        user_list = []
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            data = curser.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   active,
                   role_id,
                   task_id
            FROM User
            Where    id!=? """, [user_id]).fetchall()
            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, item[5], item[6], item[7])
                user_list.append(user)

            return user_list

    def active_users(self, user_id, new_acitve):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            curser.execute(f"""
            UPDATE user
            Set    active=?
            Where id =?""", [new_acitve, user_id])

            connection.commit()

    def add_users(self, first_name, last_name, username, password):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            curser.execute(f"""
                   INSERT INTO User (
                     first_name,
                     last_name,
                     username,
                     password

                 )
                 VALUES (
                     ?,
                     ?,
                     ?,
                     ?

                 );
                    """, [first_name, last_name, username, password])

            connection.commit()

    def update_users(self, first_name, last_name):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            curser.execute(f"""
                    UPDATE User
                   SET first_name = 'first_name',
                       last_name = 'last_name'
           
                 WHERE first_name = ? AND 
                       last_name = ?;

                        """, [first_name, last_name])

            connection.commit()

    def add_admin(self, user_id, new_status):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            curser.execute(f"""
               UPDATE user
               Set    role_id=?
               Where id =?""", [new_status, user_id])

            connection.commit()

    def add_task(self, task_name):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            curser.execute(f"""INSERT INTO Task (
                               name
                                     )
                               VALUES (
                                ?  );""", [task_name])
            connection.commit()

    def remove_task(self, task_id):
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            curser.execute(f"""
                    DELETE FROM Task
                    WHERE id = ?; """, [task_id])

            connection.commit()

    def get_tasks(self):
        task_list = []
        with sqlite3.connect(self.database_name) as connection:
            curser = connection.cursor()
            task = curser.execute("""
                   SELECT id,
                       name,
                       status
                  FROM Task;  """).fetchall()

            for item in task:
                task = Task(item[0], item[1], item[2])
                task_list.append(task)

            return task_list

    def edit_task(self, task_id, task_name, task_status):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Task
                SET 
                    name = ?,
                    status = ?
                WHERE 
                    id = ?; """, (task_name, task_status, task_id))

            connection.commit()
