from django.db import models

# Create your models here.
class AddItem(models.Model):
    title_name = models.CharField(max_length=100)
    todo_description = models.TextField()
    todo_deadline = models.DateField()