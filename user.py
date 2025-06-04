import sqlite3
# username = input("Enter your username: ")
# password= input("Enter your password: ")
def login(username, password):
    # Connect to the database
    conn = sqlite3.connect("users_db.db")
    cursor = conn.cursor()
    
    # cursor.execute(
    #     """CREATE Table users_db(
    #         username TEXT NOT NULL,
    #         password TEXT NOT NULL
    #     )
    #     """
    # )
    cursor.execute(
        """INSERT INTO users_db(username, password)
        VALUES(?, ?)
        """,
        (username, password)
    )
    # Check if the user exists in the database
    cursor.execute("SELECT * FROM users_db WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        print(f'Welcome,{username}')
        return True
    else:
        print("Invalid username or password.")
        return False
login("Emma", "Emma7777")