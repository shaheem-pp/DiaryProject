from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def entry_page(request):
    return render(request, "entry_page.html")


def view_diary(request):
    return render(request, "diary.html")

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%d %B %Y | %I:%M %p"))
