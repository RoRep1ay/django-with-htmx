from django.conf import settings
from django.db import models

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title
