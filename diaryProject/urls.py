"""diaryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from diaryApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('new_entry/', views.entry_page),
    path('view_diary/<int:id>', views.view_diary),
    # path('new_register/', views.new_register),
    path('new_diary/', views.new_diary),
    path('delete_diary/<int:id>', views.delete_diary),
    path('signout/', views.signout),
    path('edit_diary/<int:id>', views.edit_diary),
    path('edit_diary_submit/<int:id>', views.edit_diary_submit),
    path('delete_diary/<int:id>', views.delete_diary),
    # path('accounts/', include('django.contrib.auth.urls'))
]
