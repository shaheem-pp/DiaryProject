from django.db import models


# Create your models here.

class tbl_user(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)


class tbl_diary(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.CharField(max_length=20)
