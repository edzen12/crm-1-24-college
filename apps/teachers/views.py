from rest_framework import viewsets
from apps.teachers.models import Teacher
from apps.teachers.serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related(
        'user').prefetch_related('subjects')
    serializer_class = TeacherSerializer