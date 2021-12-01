from django.db import models


# Create your models here.
class Task(models.Model):
    task_item = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_item
