import sqlite3


connection = sqlite3.connect('sqlight3.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER primary key AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        is_logged_in BOOLEAN DEFAULT FALSE
    );
"""

connection.execute(create_table_query)
connection.commit()
connection.close()
