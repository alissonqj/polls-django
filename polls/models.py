from django.db import models
from django.utils import timezone
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data publicada")

    def __str__(self):
        return self.question_text

    def was_published_recently(self) -> bool:
        # return self.pub_date >= (timezone.now() - timedelta(days=1))
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
