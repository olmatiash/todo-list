from django.urls import path

from .views import (
    TaskListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUndoView,
    TaskCompleteView,
    TaskDeleteView,
    TaskUpdateView,
    TagListView,
    TaskCreateView,
)

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/complete", TaskCompleteView.as_view(), name="task-complete"),
    path("tasks/<int:pk>/undo", TaskUndoView.as_view(), name="task-undo"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
