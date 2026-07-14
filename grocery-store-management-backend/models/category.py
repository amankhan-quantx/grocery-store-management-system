from database import get_db_connection


class Category:

    @staticmethod
    def get_all():

        conn = get_db_connection()

        try:

            categories = conn.execute(
                """
                SELECT *
                FROM categories
                ORDER BY name
                """
            ).fetchall()

            return categories

        finally:

            conn.close()

    @staticmethod
    def create(name):

        conn = get_db_connection()

        try:

            conn.execute(
                """
                INSERT INTO categories(name)
                VALUES (?)
                """,
                (name,)
            )

            conn.commit()

        finally:

            conn.close()

    @staticmethod
    def get_by_id(category_id):

        conn = get_db_connection()

        try:

            category = conn.execute(
                """
                SELECT *
                FROM categories
                WHERE id = ?
                """,
                (category_id,)
            ).fetchone()

            return category

        finally:

            conn.close()

    @staticmethod
    def get_by_name(name):

        conn = get_db_connection()

        try:

            category = conn.execute(
                """
                SELECT *
                FROM categories
                WHERE LOWER(name) = LOWER(?)
                """,
                (name,)
            ).fetchone()

            return category

        finally:

            conn.close()

    @staticmethod
    def update(category_id, name):

        conn = get_db_connection()

        try:

            conn.execute(
                """
                UPDATE categories
                SET name = ?
                WHERE id = ?
                """,
                (name, category_id)
            )

            conn.commit()

        finally:

            conn.close()

    @staticmethod
    def delete(category_id):

        conn = get_db_connection()

        try:

            conn.execute(
                """
                DELETE FROM categories
                WHERE id = ?
                """,
                (category_id,)
            )

            conn.commit()

        finally:

            conn.close()