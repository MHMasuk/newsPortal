from django.contrib import admin
from .models import Category, CategoryMember

# Register your models here.

admin.site.register(CategoryMember)
admin.site.register(Category)
