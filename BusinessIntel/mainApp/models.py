from django.db import models


class Aisles(models.Model):
    aisle =models.CharField(max_length=200)
    aisle_id=models.IntegerField()

    def __str__(self):
        return self.aisle

class Department(models.Model):
    department =models.CharField(max_length=200)
    department_id=models.IntegerField()

    def __str__(self):
        return self.department

class order_products_prior(models.Model):
    department =models.CharField(max_length=200)
    order_id=models.IntegerField()
    order_id=models.IntegerField()

    def __str__(self):
        return self.department
        

