from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [ 
    path('', views.home, name="home"),
    path('category/<int:category_id>/', views.category, name="category"), 
    path('authors/<int:author_id>/', views.authors, name="author"), 
    path('recipes/<int:id>/', views.recipe, name="recipe"), #Ficaria: https://dominio.com.br/recipes/id/
]
