from database import get_db_connection


class Product:

    @staticmethod
    def get_all(
        page=1,
        per_page=10,
        sort_by="id",
        order="DESC"
    ):

        conn = get_db_connection()

        try:

            offset = (page - 1) * per_page

            allowed_columns = {
                "id",
                "name",
                "price",
                "quantity"
            }

            if sort_by not in allowed_columns:
                sort_by = "id"

            if order.upper() not in ("ASC", "DESC"):
                order = "DESC"

            products = conn.execute(
                f"""
                SELECT
                    products.*,
                    categories.name AS category_name
                FROM products
                INNER JOIN categories
                    ON products.category_id = categories.id
                ORDER BY {sort_by} {order}
                LIMIT ?
                OFFSET ?
                """,
                (per_page, offset)
            ).fetchall()

            return products

        finally:

            conn.close()

    @staticmethod
    def get_total_count():

        conn = get_db_connection()

        try:

            total = conn.execute(
                """
                SELECT COUNT(*)
                FROM products
                """
            ).fetchone()[0]

            return total

        finally:

            conn.close()

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

        try:

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

        finally:

            conn.close()

    @staticmethod
    def get_by_id(product_id):

        conn = get_db_connection()

        try:

            product = conn.execute(
                """
                SELECT *
                FROM products
                WHERE id = ?
                """,
                (product_id,)
            ).fetchone()

            return product

        finally:

            conn.close()

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

        try:

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

        finally:

            conn.close()

    @staticmethod
    def delete(product_id):

        conn = get_db_connection()

        try:

            conn.execute(
                """
                DELETE FROM products
                WHERE id = ?
                """,
                (product_id,)
            )

            conn.commit()

        finally:

            conn.close()

    @staticmethod
    def search(keyword):

        conn = get_db_connection()

        try:

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

            return products

        finally:

            conn.close()

    @staticmethod
    def get_low_stock():

        conn = get_db_connection()

        try:

            return conn.execute(
                """
                SELECT *
                FROM products
                WHERE quantity < 10
                AND quantity > 0
                ORDER BY quantity ASC
                """
            ).fetchall()

        finally:

            conn.close()
        
    @staticmethod
    def get_out_of_stock():

        conn = get_db_connection()

        try:

            return conn.execute(
                """
                SELECT *
                FROM products
                WHERE quantity = 0
                """
            ).fetchall()

        finally:

            conn.close()

    @staticmethod
    def get_recent_products(limit=5):

        conn = get_db_connection()

        try:

            products = conn.execute(
                """
                SELECT
                    products.*,
                    categories.name AS category_name
                FROM products
                INNER JOIN categories
                    ON products.category_id = categories.id
                ORDER BY products.id DESC
                LIMIT ?
                """,
                (limit,)
            ).fetchall()

            return products

        finally:

            conn.close()

    @staticmethod
    def get_expired_products():

        conn = get_db_connection()

        try:

            products = conn.execute(
                """
                SELECT *
                FROM products
                WHERE expiry_date < DATE('now')
                ORDER BY expiry_date ASC
                """
            ).fetchall()

            return products

        finally:

            conn.close()

    @staticmethod
    def get_expiring_soon_products():

        conn = get_db_connection()

        try:

            products = conn.execute(
                """
                SELECT *
                FROM products
                WHERE expiry_date BETWEEN
                    DATE('now')
                    AND
                    DATE('now', '+7 day')
                ORDER BY expiry_date ASC
                """
            ).fetchall()

            return products

        finally:

            conn.close()