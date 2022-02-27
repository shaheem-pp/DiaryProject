import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from diaryApp.models import *


# Create your views here.

@login_required()
def index(request):
    tbl = tbl_diary.objects.filter(user=request.user)
    return render(request, "index.html", {"data": tbl, "title": "Daybook"})


def entry_page(request):
    return render(request, "entry_page.html", {"title": "New | Daybook"})


def view_diary(request, id):
    tbl = tbl_diary.objects.get(id=id)
    return render(request, "diary.html", {"data": tbl, "title": tbl.title})


def new_diary(request):
    tbl = tbl_diary()
    tbl.user = request.user
    tbl.title = request.POST.get('title')
    tbl.content = request.POST.get('content')
    tbl.date = "na"
    tbl.save()
    x = datetime.datetime.now()
    tbl.date = x.strftime("Created on: %d %B %Y")
    tbl.save()
    return redirect(index)


def edit_diary(request, id):
    tbl = tbl_diary.objects.get(id=id)
    return render(request, "edit_diary.html", {"title": "Edit", "diary": tbl})


def edit_diary_submit(request, id):
    tbl = tbl_diary.objects.get(id=id)
    tbl.title = request.POST.get("Title")
    tbl.content = request.POST.get("Content")
    tbl.save()
    return redirect('/view_diary/' + str(id))


def delete_diary(request, id):
    tbl = tbl_diary.objects.get(id=id)
    tbl.delete()
    return redirect(index)
