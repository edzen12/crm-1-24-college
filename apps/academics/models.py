from django.db import models
from apps.common.models import TimeStampedModel


class Course(TimeStampedModel):
    number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f"{self.number} курс"


class Group(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='groups'
    )

    def __str__(self):
        return self.name
    

class Subject(TimeStampedModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name