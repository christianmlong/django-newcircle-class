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

    def has_answer_matching(self, pattern):
        return self.answers.filter(text__icontains=pattern).exists()


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

