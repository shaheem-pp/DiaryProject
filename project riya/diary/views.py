from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, "mainpg.html")
def login(request):
    return render(request, "login.html")
def register(request):
    return render(request, "register.html")
def content(request):
    return render(request, "content.html")   


