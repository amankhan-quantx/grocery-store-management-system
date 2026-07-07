from models.category import Category


class CategoryService:

    @staticmethod
    def get_categories():
        return Category.get_all()

    @staticmethod
    def get_category(category_id):
        return Category.get_by_id(category_id)

    @staticmethod
    def create_category(name):

        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty.")

        if len(name) > 50:
            raise ValueError("Category name cannot exceed 50 characters.")

        if Category.get_by_name(name):
            raise ValueError("Category already exists.")

        Category.create(name)

    @staticmethod
    def delete_category(category_id):

        category = Category.get_by_id(category_id)

        if not category:
            raise ValueError("Category not found.")

        Category.delete(category_id)

    @staticmethod
    def update_category(category_id, name):

        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty.")

        if len(name) > 50:
            raise ValueError("Category name cannot exceed 50 characters.")

        category = Category.get_by_id(category_id)

        if not category:
            raise ValueError("Category not found.")

        existing_category = Category.get_by_name(name)

        if (
            existing_category
            and existing_category["id"] != category_id
        ):
            raise ValueError("Category already exists.")

        Category.update(category_id, name)