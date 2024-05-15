from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Supplier(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32)
    cnpj = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    neighborhood = models.CharField(max_length=64, null=True, blank=True)
    street_number = models.CharField(max_length=64, null=True, blank=True)
    zip_code = models.CharField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    industry = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    owner_name = models.CharField(max_length=64, null=True, blank=True)
    owner_phone = models.CharField(max_length=20, null=True, blank=True)
    owner_email = models.EmailField(null=True, blank=True)
    payment_conditions = models.CharField(max_length=256, null=True, blank=True)
    delivery_time = models.IntegerField(null=True, blank=True) 
    production_time = models.IntegerField(null=True, blank=True)
    stock_consunption = models.IntegerField(null=True, blank=True)
    commission = models.FloatField(null=True, blank=True)
    fee = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)


    def __str__(self):
        return f'Supplier: {self.name}'


class Client(models.Model):
    name = models.CharField(max_length=64)
    unit = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32)
    cnpj = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    neighborhood = models.CharField(max_length=64, null=True, blank=True)
    street_number = models.IntegerField(null=True, blank=True)
    zip_code = models.CharField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    industry = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return f'Client: {self.name}'


class Product(models.Model):

    CATEGORIES = (
        ('Caixas rígidas', 'Caixas rígidas'),
        ('Papelaria', 'Papelaria'),
        ('Potes e copos', 'Potes e copos'),
        ('Adesivos e lacres', 'Adesivos e lacres'),
        ('Utensílios', 'Utensílios'),
    )

    product_name = models.CharField(max_length=64, blank=True)
    product_slug = models.SlugField(max_length=32, blank=True)
    portal_name = models.CharField(max_length=64, blank=True)
    category = models.CharField(choices=CATEGORIES, default='Sem categoria', max_length=100)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=256, blank=True)
    image = models.ImageField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    batch = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'Product: {self.product_name}'