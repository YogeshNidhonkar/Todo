""" Models of Todo app """

from django.db import models
from django.contrib.auth.models import User


STATUS = (
    ("schedule", "Schedule"),
    ("complete", "Complete"),
    ("reschedule", "Reschedule")
)

class Todo(models.Model):
    """ Class for defining todo model """
    task = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default=STATUS[0][0])
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task
