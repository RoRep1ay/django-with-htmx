from django.db import models

# Create your models here.
class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
