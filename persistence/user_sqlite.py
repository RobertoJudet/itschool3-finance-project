import sqlite3

from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User


class UserPersistenceSqlite(UserPersistenceInterface):
    def get_all(self) -> list[User]:
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM users")
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    return []
                else:
                    raise e
            users_info = cursor.fetchall()
            factory = UserFactory()
            users = [factory.make_from_persistence(x) for x in users_info]
            return users

    def add(self, user: User):
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"INSERT INTO users(id, username) VALUES ('{user.id}','{user.username}')")
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    cursor.execute("CREATE TABLE users (id TEXT PRIMARY KEY, username TEXT NOT NULL)")
                else:
                    raise e
                cursor.execute(f"INSERT INTO users(id, username) VALUES ('{user.id}','{user.username}')")
            conn.commit()

    def delete_by_id(self, user_id: User.id):
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"DELETE FROM users WHERE id='{user_id}'")
            except sqlite3.OperationalError as e:
                raise e
            conn.commit()

    def edit_by_id(self, user_id: User.id, username: str):
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    f"UPDATE users SET (username)='{username}' WHERE id='{user_id}'"
                )
            except sqlite3.OperationalError as e:
                raise e
            conn.commit()
