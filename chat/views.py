from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cigar
from django.utils import timezone
from django.shortcuts import render
from .commands import DummyData
from django.shortcuts import render, redirect
from . import dash_apps


@login_required(login_url='/login/')
def test(request):
    question = "oli oli"
    return redirect('/login/')
# Create your views here.

@login_required(login_url='login/')
def index(request):
    question = "oli oli"
    return render(request, 'index.html', {'oli': question})
@login_required(login_url='/login/')
def cigars(request):
    cigarList = Cigar.objects.order_by('-pub_date')
    context = {'cigar_List': cigarList, }
    return render(request, 'cigars.html', context)
@login_required(login_url='/login/')
def toSmoke(request):
    if request.method == 'POST':
        cigar = Cigar(stopped=-1)
        cigar.save()
        return render(request, 'index.html')
    cigar = Cigar(stopped=1)
    cigar.save()
    return render(request, 'index.html')

def execu(request):
    exec(open('/Users/piopio/PycharmProjects/DjangoHub/chat/commands/test.py').read())
    return HttpResponse("Ojala se ejecute algo")


def login(request):
    redirect('login/')
