from api_todo.views import TodoDetailAPIView, TodoListCreateAPIView, home_view
from django.urls import path

urlpatterns = [
    path("", home_view),
    # path("todolist/", todolist_view),
    # path("todocreate/", todocreate_view),
    # path("todolistcreate/", todolistcreate_view),
    # path("tododetail/<int:pk>/", tododetail_view),
    path("todolistcreateapi/", TodoListCreateAPIView.as_view()),
    path("tododetailapi/<int:pk>/", TodoDetailAPIView.as_view()),
]
