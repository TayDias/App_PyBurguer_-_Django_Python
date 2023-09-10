from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def detalhe_produto(request):
    return render(request, "produto.html")

def teste(request):
    return HttpResponse("Hello World!!!")