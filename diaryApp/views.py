import datetime

from django.shortcuts import render, redirect

# Create your views here.
from diaryApp.models import *


def index(request):
    tbl = tbl_diary.objects.all()
    return render(request, "index.html", {"data": tbl, "title": "Daybook"})


def login(request):
    return render(request, "login.html", {"title": "Login | Daybook"})


def register(request):
    return render(request, "register.html", {"title": "Register | Daybook"})


def entry_page(request):
    return render(request, "entry_page.html", {"title": "New | Daybook"})


def view_diary(request, id):
    tbl = tbl_diary.objects.get(id=id)
    return render(request, "diary.html", {"data": tbl, "title": tbl.title})


def new_register(request):
    tbl = tbl_user()
    empty = ["", " ", ".", ","]
    name = request.POST.get('fullname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if name not in empty and email not in empty and password not in empty:
        if tbl_user.objects.filter(email=email).exists():
            return redirect(register)
        else:
            tbl.name = name
            tbl.email = email
            tbl.password = password
            tbl.save()
        return redirect(index)
    return redirect(register)


def new_diary(request):
    tbl = tbl_diary()
    tbl.title = request.POST.get('title')
    tbl.content = request.POST.get('content')
    tbl.date = "na"
    tbl.save()
    x = datetime.datetime.now()
    tbl.date = x.strftime("%d %B %Y | %I:%M %p")
    tbl.save()
    return redirect(index)


def delete_diary(request, id):
    tbl = tbl_diary.objects.get(id=id)
    tbl.delete()
    return redirect(index)


def signout(request):
    return redirect(login)


def do_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if tbl_user.objects.filter(email=email, password=password).exists():
        return redirect(index)
    return redirect(login)
