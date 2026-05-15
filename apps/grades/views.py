from rest_framework import viewsets
from apps.grades.models import Grade
from apps.grades.serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related(
        'student', 'subject', 'teacher').all()
    serializer_class = GradeSerializer