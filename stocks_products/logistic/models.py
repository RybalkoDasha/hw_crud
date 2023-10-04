from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'title: {self.title}'

    class Meta:
        verbose_name_plural = 'Товары'


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )

    def __str__(self):
        return f'address: {self.address}/n products: {self.products}'

    class Meta:
        verbose_name_plural = 'Склад'


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name_plural = 'Склад-товары'

    def __str__(self):
        return f'stock: {self.stock}/n products: {self.product}/n quantity: {self.quantity}/n price: {self.price}/n'
