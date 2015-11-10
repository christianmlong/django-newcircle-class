
from django.shortcuts import render
from django.http import HttpResponse
from rest.models import Question

from rest_framework import serializers

class QuestionsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question

