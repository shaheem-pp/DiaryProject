from django.urls import path
from .views import create_diary, detail_diaries, edit_diary, list_diaries
app_name = 'diaries'

urlpatterns = [
    path('', list_diaries, name='list'),
    path('<int:id>/', detail_diaries, name='detail'),
    path('create/', create_diary, name='create'),
    path('edit/<int:id>/', edit_diary, name='edit'),
]
