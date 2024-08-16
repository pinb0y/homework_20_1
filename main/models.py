from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(verbose_name="картинка")
    category = models.ForeignKey(verbose_name="Категория")
    price = models.IntegerField(verbose_name="цена за покупку")
    create_date = models.DateTimeField(verbose_name="Дата создания")
    change_date = models.DateTimeField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.product_name}, {self.description}, {self.category}, {self.create_date}, {self.change_date}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="категория")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.category_name}, {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
