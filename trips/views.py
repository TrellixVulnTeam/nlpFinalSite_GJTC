from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from trips.models import Queries
from trips.query import Cal
# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world. You are at the pool index.")

def index(request):
    answers=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        answers = Cal(search)
        return render(request, 'index.html',{
            'questions': answers,'search':search
        })
    else:
        return render(request, 'index.html',{
            'questions': [],
        })
def welcome(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html', locals())
        



