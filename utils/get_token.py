import sqlite3
def getToken():
    # Path to your local SQLite database
    db_path = "local_db.sqlite"
    
        # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

        # Query to fetch the token
    cursor.execute("SELECT access_token FROM users LIMIT 1")
    result = cursor.fetchone()


    token = result[0]  # Retrieve the token value from the query result
    return token