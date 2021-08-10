from api_todo.views import home_view, todocreate_view, tododetail_view, todolist_view, todolistcreate_view
from django.urls import path

urlpatterns = [
    path("", home_view),
    path("todolist/", todolist_view),
    path("todocreate/", todocreate_view),
    path("todolistcreate/", todolistcreate_view),
    path("tododetail/<int:pk>/", tododetail_view),
]
