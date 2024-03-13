from rest_framework import serializers
from .models import Task, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['age']


class TaskSerializer(serializers.ModelSerializer):
    user_age = serializers.SerializerMethodField()

    def get_user_age(self, obj):
        user = obj.user
        if user:
            if hasattr(user, 'customuser'):
                return user.customuser.age
        else:
            return None

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete', 'created',
                  'user_age']
