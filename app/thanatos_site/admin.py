from django.contrib import admin
from . models import Subject, Type, Task

admin.site.register(Subject)
admin.site.register(Task)
admin.site.register(Type)
