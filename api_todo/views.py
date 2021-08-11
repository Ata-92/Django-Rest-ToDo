from api_todo.models import Todo
from api_todo.serializers import TodoSerializer
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .pagination import SmallPagination, LargePagination

# Create your views here.

def home_view(request):
    return HttpResponse("""<center><h1 style="background-color: aqua;">Welcome to ToDo App</h1></center>""")

# @api_view(["GET"])
# def todolist_view(request):
#     queryset = Todo.objects.all()
#     serializer = TodoSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(["POST"])
# def todocreate_view(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(["GET", "POST"])
# def todolistcreate_view(request):
#     if request.method == "GET":
#         queryset = Todo.objects.all()
#         serializer = TodoSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TodoListCreateAPIView(APIView):
#     def get(self, request):
#         queryset = Todo.objects.all()
#         serializer = TodoSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoListCreateConcreteView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = SmallPagination

# @api_view(["GET", "PUT", "DELETE"])
# def tododetail_view(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class TodoDetailAPIView(APIView):
#     def get_object(self, pk):
#         todo = get_object_or_404(Todo, pk=pk)
#         return todo

#     def get(self, _, pk):
#         todo = self.get_object(pk=pk)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         todo = self.get_object(pk=pk)
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, _, pk):
#         todo = self.get_object(pk=pk)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class TodoDetailConcreteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
