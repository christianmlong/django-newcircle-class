from django.shortcuts import render
from django.http import HttpResponse
from rest.models import Question
from rest.models import Answer
from rest.models import User

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from serializers import QuestionsSerializer
from serializers import AnswersSerializer
# from serializers import UsersSerializer

import time
from hendrix.experience import crosstown_traffic

def hello_world(request):
    return render(
        request,
        "hello_questions.html",
        {"message" : Question.objects.all()},
    )

def hello_async(request):

    @crosstown_traffic()
    def long_time():
        for i in range(20):
            time.sleep(.2)
            print "Counter %s" % i

    return render(
        request,
        "hello_questions.html",
        {"message" : Question.objects.all()},
    )


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer

    @detail_route()
    def has_matching_answer(self, request, pk=None):
        q = self.get_object()
        pattern = request.GET['pattern']
        has_match = q.has_answer_matching(pattern)
        # return Response(pattern)
        return Response(has_match)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer

