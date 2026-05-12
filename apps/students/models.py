from django.db import models

from apps.common.models import TimeStampedModel
from apps.academics.models import Group


class StudentStatus(models.TextChoices):
    ACTIVE = 'active', 'Учится'
    ACADEMIC = 'academic', 'Академ'
    EXPELLED = 'expelled', 'Отчислен'


class Student(TimeStampedModel):
    full_name = models.CharField(max_length=255)
    inn = models.CharField(max_length=15, unique=True)
    id_card = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=12)
    group = models.ForeignKey(
        Group, on_delete=models.PROTECT, related_name='students'
    )
    status = models.CharField(
        max_length=20, choices=StudentStatus,
        default=StudentStatus.ACTIVE
    )
    
    def __str__(self):
        return self.full_name