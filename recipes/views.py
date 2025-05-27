from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Cliente (Request) -> Servidor (Response)
# Cliente (Request) <- Servidor (Response)

# HTTP REQUEST ou Render
def home(request): # http pede envia uma request e ele retorna um http response ou render
    return render(request, 'recipes/pages/home.html', context={
        'name': 'André Henrique'
    })

def recipe(request, id): # http pede envia uma request e ele retorna um http response ou render
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'André Henrique'
    })
