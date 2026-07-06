from database import get_db_connection


class User:

    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        conn.close()

        return user

    @staticmethod
    def create(username, password_hash, role):
        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO users
            (username, password_hash, role)
            VALUES (?, ?, ?)
            """,
            (username, password_hash, role)
        )

        conn.commit()
        conn.close()