from django.shortcuts import render

from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):

    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        "recipes": recipes,
    })

def category(request, category_id):
    
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published = True,
    )
    contexto = {
        "recipes": recipes,
    }
    return render(request, 'recipes/pages/category.html', contexto)

def authors(request, author_id):
    
    recipes = Recipe.objects.filter(
        author__id=author_id,
        is_published = True,
    )
    contexto = {
        "recipes": recipes,
    }
    return render(request, 'recipes/pages/authors.html', contexto)

def recipe(request, id):

    recipe = Recipe.objects.filter(
        pk=id,
        is_published = True,
    ).order_by('-id').first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })
