from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request,'main/index.html')

def about(request):
    return render (request,'main/about.html',{'title': 'О нас'})

def catalog(request):
    data = {
        'title': 'Каталог',
        'obj': {
            'car ': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render (request,'main/catalog.html',data)

def cabinet(request):
    return render (request,'main/cabinet.html')