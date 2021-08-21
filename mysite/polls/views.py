from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

#HttpResponse specific view function

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) 
    #render(request object, template name, dictionary (optional))

def detail(request, question_id):
    return HttpResponse("YOu're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of the questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)