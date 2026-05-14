from rest_framework import serializers
from apps.academics.models import Course, Group, Subject


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields='__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields='__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields='__all__'