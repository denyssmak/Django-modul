from django.db import models
from django import forms
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class MyUser(AbstractUser):
	wallet = models.IntegerField(default=2500)




class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	quantity = models.IntegerField()
	price = models.IntegerField()

	def __str__(self):
		return self.name
		


class Purchase(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
	time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
	quantity = models.PositiveSmallIntegerField()
	def __str__(self):
		return f'{self.product} | {self.quantity}'


class PurchaseReturns(models.Model):
	product_return = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='product_return')
	product_return_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.product_return}'