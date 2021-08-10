from django.contrib import admin
from api_todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ["task", "description", "priority", "done"]

admin.site.register(Todo, TodoAdmin)
