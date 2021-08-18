from django.shortcuts import render
from django.http import HttpResponse

#HttpREsponse specific view function

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

