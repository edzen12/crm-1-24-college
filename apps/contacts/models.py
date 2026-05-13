from django.db import models
from apps.common.models import TimeStampedModel
from apps.students.models import Student


class RelationShipType(models.TextChoices):
    FATHER = 'father', 'Отец'
    MOTHER = 'mother', 'Мать'
    BROTHER = 'brother', 'Брат'
    SISTER = 'sister', 'Сестра'
    GRANDFATHER = 'grandfather', 'Дедушка'
    GRANDMOTHER = 'grandmother', 'Бабушка'
    GUARDIAN = 'guardian', 'Опекун'
    OTHER = 'other', 'Другое'


class Contact(TimeStampedModel):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='contacts'
    )
    full_name = models.CharField(max_length=200)
    relationship = models.CharField(
        max_length=20, choices=RelationShipType.choices
    )
    phone_number = models.CharField(max_length=14)
    is_primary = models.BooleanField(default=False)#главный контакт

    def __str__(self):
        return f"{self.full_name} ({self.student.full_name})"
