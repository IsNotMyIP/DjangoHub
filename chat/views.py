from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Cigar
from django.utils import timezone
from django.shortcuts import render

# Create your views here.
def index(request):
    question = "oli oli"
    return render(request, 'index.html', {'oli': question})

def toSmoke(request):

    if(request.POST):
        print("Ha")
    cigar = Cigar(stopped=False)
    cigar.save()
    return HttpResponse("Received")

def execu(request):
    exec(open('/Users/piopio/PycharmProjects/DjangoHub/chat/commands/test.py').read())
    return HttpResponse("Ojala se ejecute algo")
