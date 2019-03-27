"""my database file, creating tables and a database connection"""
import psycopg2
import os
from psycopg2.extras import RealDictCursor


class DatabaseConnection:
    """
    Initializing my database
    """
    def __init__(self):
        self.commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    password VARCHAR(200) NOT NULL, 
                    as_admin BOOLEAN DEFAULT FALSE NOT NULL
                    )

            """,
            """
                 CREATE TABLE IF NOT EXISTS car_booking (                    
                    booking_id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(user_id),
                    first_name VARCHAR(20) NOT NULL,
                    last_name VARCHAR(20) NOT NULL,
                    trip_destination VARCHAR(20) NOT NULL,
                    pourpose VARCHAR(20) NOT NULL,
                    depature_time VARCHAR(20) NOT NULL,
                    expected_return_time VARCHAR(20) NOT NULL,
                    status BOOLEAN  DEFAULT FALSE NOT NULL

                )
            """,
            """
                 CREATE TABLE IF NOT EXISTS room_booking (                    
                    room_booking_id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(user_id),
                    room_name VARCHAR(20) NOT NULL,
                    meeting_name VARCHAR(20) NOT NULL,
                    start_time VARCHAR(20) NOT NULL,
                    end_time VARCHAR(20) NOT NULL,
                    meeting_duration VARCHAR(20) NOT NULL,
                    status BOOLEAN  DEFAULT FALSE NOT NULL

                )
            """
        )
        try:

            if os.getenv("FLASK_ENV") == "production":
                self.credentials_heroku = """
                            dbname='deipk3r58od4el' 
                            user= 'aknlwxnofjeegn'
                            password = '538e8ddb510fc957f338a5b5ce6c0a941b8a4c17ee95286fa1301738d83e4632' 
                            host='ec2-50-19-109-120.compute-1.amazonaws.com' 
                            port =5432 
                            
                            """
                self.credentials = self.credentials_heroku

            elif os.getenv("FLASK_ENV") == "TESTING":
                print('Connecting to test db')
                self.connection = psycopg2.connect(dbname='test_booking',
                                                   user='postgres',
                                                   password='masete',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            else:
                print('Connecting development db')
                self.connection = psycopg2.connect(dbname='booking',
                                                   user='postgres',
                                                   password='masete',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)

            self.connection = psycopg2.connect(self.credentials, cursor_factory=RealDictCursor)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            for command in self.commands:
                self.cursor.execute(command)
        except Exception as error:
            print(f"error: {error}")

        self.cursor.execute("SELECT * FROM users WHERE email= '{}'".format("admin@gmail.com"))
        if self.cursor.fetchone():
            return None
        # set admin user

        sql = "INSERT INTO users(username, email, password, as_admin) VALUES('admin', 'admin@gmail.com', 12345, True)"

        self.cursor.execute(sql)
        self.connection.commit()

    """
    method to drop tables being used in my tests
    """
    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {} CASCADE"
        table_names = ["car_booking, users"]
        for name in table_names:
            self.cursor.execute(query.format(name))

    def create_tables(self):
        for command in self.commands:
            self.cursor.execute(command)

