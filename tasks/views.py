from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

from tasks.forms import TaskForm, TagForm
from tasks.models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "task_list"
    ordering = ["-is_done", "-created"]


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_update.html"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:index")


class TaskCompleteView(View):
    def get(self, request, pk) -> HttpResponse:
        task = Task.objects.get(pk=pk)
        task.is_done = True
        task.save()
        return redirect("tasks:index")


class TaskUndoView(View):
    def get(self, request, pk) -> HttpResponse:
        task = Task.objects.get(pk=pk)
        task.is_done = False
        task.save()
        return redirect("tasks:index")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_create.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_update.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")
