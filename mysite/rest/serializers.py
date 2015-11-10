
from django.shortcuts import render
from django.http import HttpResponse
from rest.models import Question
from rest.models import Answer

from rest_framework import serializers

class QuestionsSerializer(serializers.HyperlinkedModelSerializer):

    answers = serializers.StringRelatedField(
    # answers = serializers.PrimaryKeyRelatedField(
        # read_only=True,
        many=True,
    )

    class Meta:
        model = Question

class AnswersSerializer(serializers.HyperlinkedModelSerializer):

    answerer = serializers.StringRelatedField()

    class Meta:
        model = Answer

