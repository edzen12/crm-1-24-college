from rest_framework.routers import DefaultRouter
from apps.students.views import StudentViewSet
from apps.academics.views import (
    CourseViewSet, GroupViewSet, SubjectViewSet
)

router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('groups', GroupViewSet, basename='groups')
router.register('subjects', SubjectViewSet, basename='subjects')


