from django.shortcuts import render
from django.http import HttpResponse
from rest.models import Question
from rest.models import Answer
from rest.models import User

from rest_framework import viewsets
from serializers import QuestionsSerializer
from serializers import AnswersSerializer
from serializers import UsersSerializer


def hello_world(request):
    # temp = []
    # for index, question in enumerate(Question.objects.all()):
    #     temp.append("%s %s" % (index, question))

    # rendered_text = '<br>'.join(temp)

    return render(
        request,
        "hello_questions.html",
        {"message" : Question.objects.all()},
    )


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

