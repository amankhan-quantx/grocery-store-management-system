from models.product import Product


class ProductService:

    @staticmethod
    def get_products():
        return Product.get_all()

    @staticmethod
    def create_product(
        name,
        category,
        description,
        price,
        quantity,
        image,
        supplier
    ):

        Product.create(
            name,
            category,
            description,
            price,
            quantity,
            image,
            supplier
        )