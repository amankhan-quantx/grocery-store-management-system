from models.product import Product


class ProductService:

    @staticmethod
    def get_products(
        page=1,
        per_page=10,
        sort_by="id",
        order="DESC"
    ):

        return Product.get_all(
            page,
            per_page,
            sort_by,
            order
        )

    @staticmethod
    def get_product(product_id):

        return Product.get_by_id(product_id)
    
    @staticmethod
    def get_total_products():

        return Product.get_total_count()
    
    @staticmethod
    def get_low_stock():

        return Product.get_low_stock()

    @staticmethod
    def get_out_of_stock():

        return Product.get_out_of_stock()
    
    @staticmethod
    def get_recent_products():

        return Product.get_recent_products()
    
    @staticmethod
    def get_expired_products():

        return Product.get_expired_products()


    @staticmethod
    def get_expiring_soon_products():

        return Product.get_expiring_soon_products()

    @staticmethod
    def create_product(
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

        Product.create(
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

    @staticmethod
    def update_product(
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

        Product.update(
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
        )

    @staticmethod
    def delete_product(product_id):

        Product.delete(product_id)

    @staticmethod
    def search_products(keyword):

        return Product.search(keyword)