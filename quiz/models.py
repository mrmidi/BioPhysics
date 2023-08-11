from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=255, default="Undefined")


class Question(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_DEFAULT, default=None, null=True)


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class UserAnswerHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)
    was_correct = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

