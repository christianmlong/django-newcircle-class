# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest', '0003_auto_20151110_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answerer',
            field=models.ForeignKey(related_name='answers_authored', default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
