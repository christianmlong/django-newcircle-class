from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Question
    """
    text = models.CharField(max_length=80)
    test = models.CharField(max_length=120)

    def __unicode__(self):
        return self.text

class Answer(models.Model):
    """
    Answer
    """
    text = models.CharField(max_length=255)
    question = models.ForeignKey(
        Question,
        related_name='answers',
    )
    answerer = models.ForeignKey(
        User,
        related_name='answers_authored',
    )

    def __unicode__(self):
        return self.text

