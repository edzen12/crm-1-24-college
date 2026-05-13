from django.contrib import admin
from apps.academics.models import Group, Subject, Course, TeachingAssignment


admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(TeachingAssignment)