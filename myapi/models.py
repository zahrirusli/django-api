from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=255)
