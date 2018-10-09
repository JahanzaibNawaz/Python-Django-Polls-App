
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    # template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html')
    # return render(request, 'polls/index.html', context)
    
def detail(request,question_id):
    return HttpResponse("You are looking at Question %s." % question_id)

def result(request, question_id):
    response = " Welcome to Question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)

