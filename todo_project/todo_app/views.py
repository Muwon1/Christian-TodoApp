from django.shortcuts import render, Register
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,, RegisterPage
from. django.contrib.auth.views import LoginView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login




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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            queryset = queryset.filter(title__startswith=search_input)

        return queryset

       
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['object_list'] = context['object_list'].filter(user=self.request.user)
            context['count'] = context['object_list'].filter(complete=False).count()
    
    
             search_input = self.request.GET.get('search-area') or ''
                if search_input:
                    context['object_list'] = context['object_list'].filter(title__startswith=search_input)
                context['search_input'] = search_input
            return context
class RegisterPage(FormView):
    template_name ='todo_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
        def form_valid(self, form):
            user = form.save()
            if user is not None:
            login(self.request, user)
            return super(RegisterPage, self).form_valid(form)
    
        def get(self, *args, **kwargs):
            if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):    
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            tasks = self.get_queryset()
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': 'You need to be logged in to access this endpoint.'}, status=401)

