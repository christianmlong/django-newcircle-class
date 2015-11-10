
from django.shortcuts import render
from django.http import HttpResponse
from rest.models import Question
from rest.models import Answer
from django.contrib.auth.models import User

from rest_framework import serializers

class QuestionsSerializer(serializers.HyperlinkedModelSerializer):

    answers = serializers.StringRelatedField(
        many=True,
    )

    class Meta:
        model = Question

class AnswersSerializer(serializers.HyperlinkedModelSerializer):

    # answerer = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    # )
    answerer = serializers.StringRelatedField(
        read_only=True,
    )
    question = serializers.StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = Answer
        fields = ('text', 'answerer', 'question')

class UsersSerializer(serializers.HyperlinkedModelSerializer):

    answers_authored = serializers.StringRelatedField(
        many=True,
    )

    class Meta:
        model = User
        fields = ('id', 'email')

