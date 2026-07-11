from models.product import Product


class ProductService:

    @staticmethod
    def get_products():

        return Product.get_all()

    @staticmethod
    def get_product(product_id):

        return Product.get_by_id(product_id)

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