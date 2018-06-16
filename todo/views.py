from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from todo.forms import TodoForm
from todo.models import Todo


class TodoList(ListView):
    model = Todo
    template_name = 'index.html'


class TodoDetail(DetailView):
    model = Todo
    template_name = 'detail.html'


class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create.html'


class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create.html'


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('index')
