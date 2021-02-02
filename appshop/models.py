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
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user')
	time = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product')
	quantity_purchase = models.IntegerField()


class Purchase_returns(models.Model):
	product_return = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_return')
	product_return_time = models.DateTimeField(auto_now_add=True)