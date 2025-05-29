from django.contrib import admin
from .models import category, Recipe

# Register your models here.
@admin.register(category)
class CategoriaAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
