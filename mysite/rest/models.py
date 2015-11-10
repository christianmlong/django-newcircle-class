from django.db import models


class Question(models.Model):
    """
    Question
    """
    text = models.CharField(max_length=80)
    test = models.CharField(max_length=120)

    def __unicode__(self):
        return self.text

