from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Diary(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.created_by}'
