from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Администратор'
    TEACHER = 'teacher', 'Преподаватель'
    CURATOR = 'curator', 'Куратор'
    STUDENT = 'student', 'Студент'


class User(AbstractUser):
    role = models.CharField(
        max_length=20, 
        choices=UserRole.choices
    )

    def __str__(self):
        return self.username