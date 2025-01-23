import sqlite3

class DatabaseManager:
    def __init__(self, db_name="local_db.sqlite"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        """Establish a connection to the database."""
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        """Create necessary tables."""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            gender TEXT,
            status TEXT,
            access_token TEXT
        )
        """
        self.execute_query(query)

    def execute_query(self, query, params=None):
        """Execute a query in the database."""
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        conn.close()

    def fetch_one(self, query, params=None):
        """Fetch a single record from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        return result

    def fetch_all(self, query, params=None):
        """Fetch all records from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    def save_user_data(self, user_data):
        """Save user data to the database."""
        query = """
        INSERT INTO users (id, first_name, last_name, email, phone, gender, status, access_token)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            user_data['user']['id'],
            user_data['user']['firstName'],
            user_data['user']['lastName'],
            user_data['user']['email'],
            user_data['user']['phone'],
            user_data['user']['gender'],
            user_data['user']['status'],
            user_data['access_token']
        )
        self.execute_query(query, params)

    def get_user_data(self):
        """Retrieve user data from the database."""
        query = "SELECT * FROM users LIMIT 1"
        return self.fetch_one(query)

    def clear_user_data(self):
        """Clear user data from the database."""
        query = "DELETE FROM users"
        self.execute_query(query)
