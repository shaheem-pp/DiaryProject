from django.shortcuts import redirect, render

from diaries.forms import DiaryCreateForm, SignupForm

from .models import Diary

from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = SignupForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required
def list_diaries(request):
    diaries = Diary.objects.filter(created_by=request.user)
    context = {'diaries': diaries}
    return render(request, 'diaries/list.html', context)


@login_required
def detail_diaries(request, id):
    diary = Diary.objects.get(id=id)
    context = {'diary': diary}
    return render(request, 'diaries/detail.html', context)


@login_required
def create_diary(request):
    form = DiaryCreateForm()
    context = {'form': form}
    if request.POST:
        form = DiaryCreateForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.created_by = request.user
            diary.save()
            return redirect('diaries:list')
    return render(request, 'diaries/create.html', context)


@login_required
def edit_diary(request, id):
    diary = Diary.objects.get(id=id)
    form = DiaryCreateForm(instance=diary)
    context = {'form': form}
    if request.POST:
        form = DiaryCreateForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.created_by = request.user
            diary.save()
            return redirect('diaries:list')
    return render(request, 'diaries/edit.html', context)
