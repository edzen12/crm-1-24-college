from django.contrib import admin
from apps.academics.models import Group, Subject, Course


admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Course)