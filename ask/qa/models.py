from django.db import models

# Create your models here.

class QuestionManager(models.Manager):
        def new():
                return self.order_by('-added_at')
        def popular():
                return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
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
