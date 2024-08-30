from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.SmallIntegerField()
    decesiver = models.SmallIntegerField()
    message = models.TextField()
