from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name="Ссылка на категорию")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
