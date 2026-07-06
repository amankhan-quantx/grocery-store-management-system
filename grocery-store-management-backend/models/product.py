from database import get_db_connection


class Product:

    @staticmethod
    def get_all():
        conn = get_db_connection()

        products = conn.execute(
            "SELECT * FROM products ORDER BY id DESC"
        ).fetchall()

        conn.close()

        return products

    @staticmethod
    def create(
        name,
        category,
        description,
        price,
        quantity,
        image,
        supplier
    ):

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO products
            (
                name,
                category,
                description,
                price,
                quantity,
                image,
                supplier
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                category,
                description,
                price,
                quantity,
                image,
                supplier
            )
        )

        conn.commit()
        conn.close()