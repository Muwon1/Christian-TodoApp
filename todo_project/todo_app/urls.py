from django.urls import path, include
from .views import (TaskList, TaskDetail, TaskCreate,
                    TaskUpdate, DeleteView, CustomLoginView,
                    RegisterPage)

from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [

    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', DeleteView.as_view(), name='task-delete'),
    path('api/', include(router.urls)),
]
