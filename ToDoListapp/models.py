from django.db import models
class todoData(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=100)
    Description=models.CharField(max_length=255)
