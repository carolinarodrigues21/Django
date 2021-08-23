from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.template import loader

from .models import Choice, Question 

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

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #let's you access submitted data by key name; returns the ID of the selected choice as a string.
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question, 
            'error_message':"You didn't select a choice.",
        })

    else: 
        selected_choice.votes +=1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})