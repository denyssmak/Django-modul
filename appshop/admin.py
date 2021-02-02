from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Product, Purchase, Purchase_returns

admin.site.register(MyUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Purchase_returns)