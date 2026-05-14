from rest_framework.viewsets import ModelViewSet
from apps.academics.models import Course, Subject, Group
from apps.academics.serializers import (
    CourseSerializer, SubjectSerializer, GroupSerializer
)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.select_related('course').all()
    serializer_class = GroupSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer