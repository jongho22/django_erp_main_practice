from django.contrib import admin
from .models import Product, COA, User, Department, Incumbent

# Register your models here.
admin.site.register(Product)
admin.site.register(COA)
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Incumbent)