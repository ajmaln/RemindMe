from django.db import models
from django.urls import reverse


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view-todo', kwargs={'pk': self.id})
