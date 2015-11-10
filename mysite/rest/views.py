from django.shortcuts import render
from django.http import HttpResponse
from rest.models import Question

from rest_framework import viewsets
from serializers import QuestionsSerializer


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

