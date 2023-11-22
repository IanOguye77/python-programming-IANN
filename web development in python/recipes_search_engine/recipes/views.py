from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def homepage(request):
    app_id = "11c47915"
    app_key = "84e47fff6921dc4108d3c29bd40ab962"
    url = "https://api.edamam.com/api/recipes/v2?type=public&q=cheese&app_id=11c47915&app_key=%2084e47fff6921dc4108d3c29bd40ab962"
    req = requests.get(url)
    response = req.json()
    recipes = response["hits"]
    return render(request, "recipes/index.html", {
        "recipes": recipes
    })