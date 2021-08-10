from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    TITLES = [
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low")
    ]
    priority = models.CharField(max_length=50, choices=TITLES)

    def __str__(self):
        return self.task
