from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=128, default='Попугай')
    category_picture = models.ImageField(upload_to='media', blank=True, verbose_name='изображение' )
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(default='0', max_length=128)
    link = models.URLField(default=0, max_length=128)
    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    FIO = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    def __str__(self):
        return self.FIO

