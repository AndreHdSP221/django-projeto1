from django.contrib.auth.models import User
from django.db import models

class category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

# Recipe = tabelas, parametros = colunas
class Recipe(models.Model):
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=10)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=10)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        default=False
    )
    cover = models.ImageField(upload_to='recipe/covers/%Y/%m/%d/') # media/recipe/covers/%Y/%m/%d/ 
    category = models.ForeignKey(
        category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None #None == Null
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default= None
    )

    def __str__(self):
        return self.title