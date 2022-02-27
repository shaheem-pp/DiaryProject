from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class tbl_diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.CharField(max_length=20)
