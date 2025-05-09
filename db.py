import sqlite3

def create_database():
    """Creates the database and tables."""
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            preferences TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Conversations (
            conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            timestamp TEXT,
            user_message TEXT,
            chatbot_response TEXT,
            FOREIGN KEY (user_id) REFERENCES Users (user_id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

def insert_user(name, age, preferences):
    """Inserts a new user into the Users table."""
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (name, age, preferences) VALUES (?, ?, ?)", (name, age, preferences))
    conn.commit()
    conn.close()
    print(f"User '{name}' inserted successfully.")

def insert_conversation(user_id, timestamp, user_message, chatbot_response):
    """Inserts a new conversation into the Conversations table."""
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Conversations (user_id, timestamp, user_message, chatbot_response) VALUES (?, ?, ?, ?)", (user_id, timestamp, user_message, chatbot_response))
    conn.commit()
    conn.close()
    print("Conversation inserted successfully.")

def get_conversation_history(user_id):
    """Retrieves conversation history for a given user."""
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, user_message, chatbot_response FROM Conversations WHERE user_id = ?", (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history

if __name__ == "__main__":
    create_database()
    insert_user("John Doe", 75, "Large font")
    insert_conversation(1, "2023-10-27 10:00:00", "Hello", "Hi there!")
    history = get_conversation_history(1)
    print("Conversation History:")
    for row in history:
        print(row)