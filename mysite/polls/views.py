from django.shortcuts import render
from django.http import HttpResponse

#HttpREsponse specific view function

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("YOu're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of the questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)