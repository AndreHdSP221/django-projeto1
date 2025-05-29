from django.shortcuts import render

from utils.recipes.factory import make_recipe

# Create your views here.
# Cliente (Request) -> Servidor (Response)
# Cliente (Request) <- Servidor (Response)

# HTTP REQUEST ou Render
def home(request): # http pede envia uma request e ele retorna um http response ou render
    return render(request, 'recipes/pages/home.html', context={
        "recipes": [make_recipe() for _ in range(10)],
    })

def recipe(request, id): # http pede envia uma request e ele retorna um http response ou render
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datail_page': True,
    })
