import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("Executing:", query)

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


if __name__ == "__main__":
    user_input = input("Enter username: ")
    users = get_user(user_input)

    for user in users:
        print(user)