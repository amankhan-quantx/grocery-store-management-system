from database import get_db_connection


class Product:

    @staticmethod
    def get_all():

        conn = get_db_connection()

        products = conn.execute(
            """
            SELECT
                products.*,
                categories.name AS category_name
            FROM products
            INNER JOIN categories
                ON products.category_id = categories.id
            ORDER BY products.id DESC
            """
        ).fetchall()

        conn.close()

        return products

    @staticmethod
    def create(
        name,
        category_id,
        description,
        price,
        quantity,
        supplier,
        barcode,
        expiry_date,
        image
    ):

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO products
            (
                name,
                category_id,
                description,
                price,
                quantity,
                supplier,
                barcode,
                expiry_date,
                image
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                category_id,
                description,
                price,
                quantity,
                supplier,
                barcode,
                expiry_date,
                image
            )
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(product_id):

        conn = get_db_connection()

        product = conn.execute(
            """
            SELECT *
            FROM products
            WHERE id = ?
            """,
            (product_id,)
        ).fetchone()

        conn.close()

        return product

    @staticmethod
    def update(
        product_id,
        name,
        category_id,
        description,
        price,
        quantity,
        supplier,
        barcode,
        expiry_date,
        image
    ):

        conn = get_db_connection()

        conn.execute(
            """
            UPDATE products
            SET
                name = ?,
                category_id = ?,
                description = ?,
                price = ?,
                quantity = ?,
                supplier = ?,
                barcode = ?,
                expiry_date = ?,
                image = ?
            WHERE id = ?
            """,
            (
                name,
                category_id,
                description,
                price,
                quantity,
                supplier,
                barcode,
                expiry_date,
                image,
                product_id
            )
        )

        conn.commit()
        conn.close()

    @staticmethod
    def delete(product_id):

        conn = get_db_connection()

        conn.execute(
            """
            DELETE FROM products
            WHERE id = ?
            """,
            (product_id,)
        )

        conn.commit()
        conn.close()
    
    @staticmethod
    def search(keyword):

        conn = get_db_connection()

        products = conn.execute(
            """
            SELECT
                products.*,
                categories.name AS category_name
            FROM products
            INNER JOIN categories
                ON products.category_id = categories.id
            WHERE products.name LIKE ?
            ORDER BY products.id DESC
            """,
            (f"%{keyword}%",)
        ).fetchall()

        conn.close()

        return products