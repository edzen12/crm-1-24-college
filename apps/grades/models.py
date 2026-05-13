from django.db import models

from apps.common.models import TimeStampedModel 
from apps.students.models import Student 
from apps.teachers.models import Teacher 
from apps.academics.models import Subject


class GradeValue(models.TextChoices):
    ZERO = '0', '0'
    ONE = '1', '1'
    TWO = '2', '2'
    THREE = '3', '3'
    FOUR = '4', '4'
    FIVE = '5', '5'
    ABSENT = 'NB', 'НБ'


class Grade(TimeStampedModel):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='grades'
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE,
        related_name='grades'
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name='grades'
    )
    value = models.CharField(
        max_length=2,
        choices=GradeValue.choices
    )
    grade_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-grade_date"]

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.value}"

