from rest_framework import serializers
from apps.grades.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields='__all__'