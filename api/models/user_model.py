from flask import jsonify
from api.models.database import DatabaseConnection


class Users:
    cursor = DatabaseConnection().cursor
    users_list = []

    def __init__(self, user_id=None, username=None, first_name=None, last_name=None, email=None, password=None, admin=False):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.admin = admin

    def add_new_user(self, username, first_name, last_name, email, password):
        query = "INSERT INTO users(username, first_name, last_name, email, password) VALUES('{}','{}','{}','{}','{}')".format(username, first_name, last_name, email, password)
        self.cursor.execute(query)
        return jsonify({"massage": "user added succefully"})

    def get_user_by_email(self, email):
        result = "SELECT * FROM users WHERE email = '{}'".format(email)
        self.cursor.execute(result)
        query1 = self.cursor.fetchone()
        if not query1:
            return False
        return query1

    # def check_password(self, hash, password):
    #     return check_password_hash(hash, password)

    # def fetch_user(self, username):
    #
    #     fetch_user_query = f""" SELECT username, password FROM users
    #            WHERE username='{username}'
    #     """
    #     response = None
    #     # 1 query db
    #     cursor.execute(fetch_user_query)
    #     # 2 fetch result
    #     fetched_user = cursor.fetchone()
    #     if fetched_user:
    #         response = fetched_user
    #     else:
    #         response = {"error": "user does not exist"}
    #     return response

    def signup_user(self, username, email):

        user_exists_query = f"""
                   SELECT username from users WHERE username='{username}'
               """

        self.cursor.execute(user_exists_query)
        returned_user = self.cursor.fetchone()
        if returned_user:
            return False

        reqister_user_query = f""" INSERT INTO users (username, email)
               VALUES('{username}', '{email}')
                    """
        self.cursor.execute(reqister_user_query)

        user_exists_query1 = f"""
                           SELECT username from users WHERE username='{username}'
                       """
        self.cursor.execute(user_exists_query1)
        user1 = self.cursor.fetchone()
        return user1

    def check_admin_status(self, user_id):
        query = "SELECT * FROM users WHERE user_id = '{}'".format(user_id)
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            user = Users(result[0], result[1], result[2])
            return user
        return None

    def get_all_users(self):
        self.users_list.clear()
        get_all_users = "SELECT * FROM users"
        self.cursor.execute(get_all_users)
        results = self.cursor.fetchall()
        self.users_list.append(results)
        return self.users_list



