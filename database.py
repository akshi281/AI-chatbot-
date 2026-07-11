import sqlite3
from datetime import datetime

DATABASE_NAME = "chatbot.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id TEXT PRIMARY KEY,
        title TEXT,
        created_at TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id TEXT,
        role TEXT,
        content TEXT,
        created_at TEXT,
        FOREIGN KEY(conversation_id)
            REFERENCES conversations(id)
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Conversation Functions
# -----------------------------

def create_conversation(conversation_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO conversations
    VALUES (?, ?, ?)
    """, (
    conversation_id,
    "New Chat",   # <-- Hardcoded
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
))

    conn.commit()
    conn.close()


def get_conversations():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM conversations
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def delete_conversation(conversation_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE conversation_id=?",
        (conversation_id,)
    )

    cursor.execute(
        "DELETE FROM conversations WHERE id=?",
        (conversation_id,)
    )

    conn.commit()

    conn.close()


# -----------------------------
# Message Functions
# -----------------------------

def save_message(conversation_id, role, content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO messages
    (conversation_id, role, content, created_at)
    VALUES (?, ?, ?, ?)
    """, (
        conversation_id,
        role,
        content,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    conn.close()


def get_messages(conversation_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT role, content
    FROM messages
    WHERE conversation_id=?
    ORDER BY id
    """, (conversation_id,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def clear_messages(conversation_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE conversation_id=?",
        (conversation_id,)
    )

    conn.commit()

    conn.close()


def update_conversation_title(conversation_id, title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE conversations
    SET title=?
    WHERE id=?
    """, (title, conversation_id))

    conn.commit()
    conn.close()


# -----------------------------
# Clear Database
# -----------------------------

def clear_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages")

    cursor.execute("DELETE FROM conversations")

    conn.commit()

    conn.close()


# -----------------------------
# Initialize Database
# -----------------------------

create_tables()

# -----------------------------
# Memory Functions
# -----------------------------

def save_memory(key, value):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO memory(memory_key, memory_value)
    VALUES(?,?)
    """, (key, value))

    conn.commit()
    conn.close()


def get_all_memory():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT memory_key,memory_value FROM memory
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]