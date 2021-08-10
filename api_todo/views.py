from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return HttpResponse("""<center><h1 style="background-color: aqua;">Welcome to ToDo App</h1></center>""")
