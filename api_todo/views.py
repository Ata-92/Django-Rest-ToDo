from api_todo.models import Todo
from api_todo.serializers import TodoSerializer
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home_view(request):
    return HttpResponse("""<center><h1 style="background-color: aqua;">Welcome to ToDo App</h1></center>""")

@api_view(["GET"])
def todolist_view(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def todocreate_view(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET", "POST"])
def todolistcreate_view(request):
    if request.method == "GET":
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
