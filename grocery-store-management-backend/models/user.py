from database import get_db_connection


class User:

    @staticmethod
    def get_by_username(username):

        conn = get_db_connection()

        try:

            user = conn.execute(
                """
                SELECT *
                FROM users
                WHERE username = ?
                """,
                (username,)
            ).fetchone()

            return user

        finally:

            conn.close()

    @staticmethod
    def create(username, password_hash, role):

        conn = get_db_connection()

        try:

            conn.execute(
                """
                INSERT INTO users
                (
                    username,
                    password_hash,
                    role
                )
                VALUES (?, ?, ?)
                """,
                (
                    username,
                    password_hash,
                    role
                )
            )

            conn.commit()

        finally:

            conn.close()