from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Cigar
from django.utils import timezone
from django.shortcuts import render
from .commands import DummyData

from . import dash_apps


def test(request):
    DummyData.chat_cigar(20)
    return render(request, 'test.html')
# Create your views here.
def index(request):
    question = "oli oli"
    return render(request, 'index.html', {'oli': question})

def cigars(request):
    cigarList = Cigar.objects.order_by('-pub_date')
    context = {'cigar_List': cigarList, }
    return render(request, 'cigars.html', context)

def toSmoke(request):
    if request.method == 'POST':
        print("holo")
        cigar = Cigar(stopped=True)
        cigar.save()
        return render(request, 'index.html')
    cigar = Cigar(stopped=False)
    cigar.save()
    return render(request, 'index.html')

def execu(request):
    exec(open('/Users/piopio/PycharmProjects/DjangoHub/chat/commands/test.py').read())
    return HttpResponse("Ojala se ejecute algo")
