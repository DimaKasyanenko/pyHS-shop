from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name="Ссылка на категорию")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название товара")
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name="Ссылка на товар")
    description = models.TextField(blank=True, null=True, verbose_name="Описание товара")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Изображение товара")
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="Цена товара")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка товара")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering: (id,)

    def __str__(self):
        return self.name

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
