import json

from django.core.management import BaseCommand

from config.settings import CATEGORIES_DIR, PRODUCTS_DIR
from main.models import Product, Category


class Command(BaseCommand):
    """
    Удаляет старые записи в БД и записывает новые из json файла.
    """

    @staticmethod
    def json_read_file(path):
        """
        Читает данные из json файла.
        :param path: Путь к json файлу
        :return: Возвращает весь файл.
        """
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def handle(self, *args, **kwargs):

        # Удаление старых записей
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создание объектов категорий
        categories_for_create = []
        for category_item in Command.json_read_file(CATEGORIES_DIR):
            categories_for_create.append(Category(**category_item["fields"]))

        Category.objects.bulk_create(categories_for_create)

        # Создание объектов продуктов
        products_for_create = []
        for product_item in Command.json_read_file(PRODUCTS_DIR):
            category = product_item["fields"].pop("category")
            product_item["fields"]["category_id"] = Category.objects.get(
                category_name=category
            ).pk
            products_for_create.append(Product(**product_item["fields"]))

        Product.objects.bulk_create(products_for_create)
