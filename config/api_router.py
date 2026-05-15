from rest_framework.routers import DefaultRouter
from apps.students.views import StudentViewSet
from apps.contacts.views import ContactViewSet
from apps.grades.views import GradeViewSet
from apps.teachers.views import TeacherViewSet
from apps.academics.views import (
    CourseViewSet, GroupViewSet, SubjectViewSet
)

router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('groups', GroupViewSet, basename='groups')
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('teachers', TeacherViewSet, basename='teachers')
router.register('contacts', ContactViewSet, basename='contacts')
router.register('grades', GradeViewSet, basename='grades')


