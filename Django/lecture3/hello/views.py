from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def balo(request):
    return HttpResponse("Hello, Balo!")

def greet(request, name):
    context = {'name': name.title()}
    return render(request, 'hello/name.html', context=context)