from django.contrib import admin
from .models import Task
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'age']


admin.site.register(Task)
admin.site.register(CustomUser)
