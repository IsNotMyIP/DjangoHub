from django.http import HttpResponse, HttpResponseRedirect
import json
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Cigar
from django.utils import timezone
from django.shortcuts import render
from .commands import DummyData
from django.shortcuts import render, redirect
from . import dash_apps


def dashboard(request):
    if request.user.is_authenticated:
        print(request.user)
        return render(request, 'test.html')
    else:
        question = "oli oli"
        return redirect('/login/')

def delete(request):
    cig_id = request.POST['id']
    print(cig_id)
    Cigar.objects.filter(id=cig_id).delete()
    return HttpResponseRedirect(reverse('chat:cigars'))
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
        cigar = Cigar(stopped=-1)
        cigar.save()
        return render(request, 'index.html')
    cigar = Cigar(stopped=1)
    cigar.save()
    return render(request, 'index.html')

def execu(request):
    exec(open('/Users/piopio/PycharmProjects/DjangoHub/chat/commands/test.py').read())
    return HttpResponse("Ojala se ejecute algo")
