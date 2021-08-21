from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

#HttpResponse specific view function

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) 
    #render(request object, template name, dictionary (optional))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pools/detail.htm', {'question': question})

    #another way to do this is:
    #try:
    #    return HttpResponse("You're looking at question %s." % question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'pools/detail.htm', {'question': question})

def results(request,question_id):
    response = "You're looking at the results of the questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)