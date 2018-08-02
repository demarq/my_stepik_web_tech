from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.CharField()
    likes = models.Charfied()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=SET_NULL)
    author = models.CharField()
