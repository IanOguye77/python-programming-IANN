from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
# def homepage(request):
#     app_id = "e6923da3"
#     app_key = "e6b537567c0ef01449a426d6c1e0da86"
#     url = "https://api.edamam.com/api/recipes/v2?type=public&q=cheese&app_id=11c47915&app_key=%2084e47fff6921dc4108d3c29bd40ab962"
#     req = requests.get(url)
#     response = req.json()
#     JobApp = response["hits"]
#     return render(request, "JobApp/index.html", {
#         "JobApp": JobApp
#     })
def homepage(request):
    return HttpResponse('<h1>THIS IS MY HOMEPAGE</h1>')
    # return render (requests, 'JobApp/index.html')