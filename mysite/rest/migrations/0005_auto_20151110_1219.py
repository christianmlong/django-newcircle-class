# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_answer_answerer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answerer',
            field=models.ForeignKey(related_name='answers_authored', to=settings.AUTH_USER_MODEL),
        ),
    ]
