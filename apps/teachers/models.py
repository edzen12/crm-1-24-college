from django.db import models

from apps.common.models import TimeStampedModel
from apps.accounts.models import User 
from apps.academics.models import Subject


class Teacher(TimeStampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='teacher_profile'
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    subjects = models.ManyToManyField(
        Subject, related_name='teachers'
    )

    def __str__(self):
        return self.full_name
