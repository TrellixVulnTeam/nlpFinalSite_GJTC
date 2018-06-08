from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from nlpFinal.Main import OutputSynonym
from collections import defaultdict

def index(request):
    answers=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        answers = OutputSynonym(search)
        return render(request, 'index.html',{
            'dictionary': answers,'search':search
        })
    else:
        return render(request, 'index.html',{
            'dictionary': [],'search':''
        })
