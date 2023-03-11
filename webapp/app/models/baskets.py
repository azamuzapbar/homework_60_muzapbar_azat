from django.db import models

class Basket(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2)