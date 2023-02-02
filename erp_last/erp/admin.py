from django.contrib import admin
from .models import Product, COA, User

# Register your models here.
admin.site.register(Product)
admin.site.register(COA)
admin.site.register(User)