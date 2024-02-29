from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,
from. django.contrib.auth.views import LoginView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin, ListView):
    model = Task 
    template_name = 'todo_app/task_list.html'
    context_object_name = 'tasks'
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):    
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
