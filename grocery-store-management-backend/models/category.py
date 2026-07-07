from database import get_db_connection


class Category:

    @staticmethod
    def get_all():

        conn = get_db_connection()

        categories = conn.execute(
            """
            SELECT *
            FROM categories
            ORDER BY name
            """
        ).fetchall()

        conn.close()

        return categories

    @staticmethod
    def create(name):

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO categories(name)
            VALUES (?)
            """,
            (name,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(category_id):

        conn = get_db_connection()

        category = conn.execute(
            """
            SELECT *
            FROM categories
            WHERE id = ?
            """,
            (category_id,)
        ).fetchone()

        conn.close()

        return category
    
    @staticmethod
    def get_by_name(name):

        conn = get_db_connection()

        category = conn.execute(
            """
            SELECT *
            FROM categories
            WHERE LOWER(name) = LOWER(?)
            """,
            (name,)
        ).fetchone()

        conn.close()

        return category
    
    @staticmethod
    def delete(category_id):

        conn = get_db_connection()

        conn.execute(
            """
            DELETE FROM categories
            WHERE id = ?
            """,
            (category_id,)
        )

        conn.commit()

        conn.close()

    @staticmethod
    def update(category_id, name):

        conn = get_db_connection()

        conn.execute(
            """
            UPDATE categories
            SET name = ?
            WHERE id = ?
            """,
            (name, category_id)
        )

        conn.commit()

        conn.close()
    
    