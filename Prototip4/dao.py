import sqlite3
from typing import Optional, Dict, Any

DB_PATH = "prototip4.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    token TEXT
);
"""

SAMPLE_USERS = [
    {
        "username": "mare",
        "password": "mare",
        "email": "prova@gmail.com",
        "token": "token12345",
    },
    {
        "username": "pare",
        "password": "pare",
        "email": "prova2@gmail.com",
        "token": "token67890",
    },
]


def initialize_database(db_path: str = DB_PATH) -> None:
    """Create the SQLite database and populate the users table."""
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(CREATE_TABLE_SQL)
        conn.commit()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM User")
        count = cursor.fetchone()[0]
        if count == 0:
            for user in SAMPLE_USERS:
                conn.execute(
                    "INSERT INTO User (username, password, email, token) VALUES (?, ?, ?, ?)",
                    (user["username"], user["password"], user["email"], user["token"]),
                )
            conn.commit()
    finally:
        conn.close()


class UserDAO:
    def __init__(self, db_path: str = DB_PATH) -> None:
        self.db_path = db_path
        initialize_database(self.db_path)

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def login(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate a user by username or email and password."""
        sql = "SELECT id, username, email, token FROM User WHERE (username = ? OR email = ?) AND password = ?"
        conn = self._connect()
        try:
            cursor = conn.execute(sql, (username, username, password))
            row = cursor.fetchone()
            if row:
                user_id, username_val, email, token = row
                return {
                    "id": user_id,
                    "username": username_val,
                    "email": email,
                    "token": token or "",
                    "idrole": 1,
                }
            return None
        finally:
            conn.close()

    def login_with_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Authenticate a user by token."""
        sql = "SELECT id, username, email, token FROM User WHERE token = ?"
        conn = self._connect()
        try:
            cursor = conn.execute(sql, (token,))
            row = cursor.fetchone()
            if row:
                user_id, username_val, email, token_val = row
                return {
                    "id": user_id,
                    "username": username_val,
                    "email": email,
                    "token": token_val,
                    "idrole": 2,
                }
            return None
        finally:
            conn.close()
