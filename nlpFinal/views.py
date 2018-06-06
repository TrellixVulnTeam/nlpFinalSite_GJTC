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
        '''
        answers = {"Synset('plant_n_01')": 
                         {'def': 'buildings for carrying on industrial labor',
                          'ex': 'they built a large plant to manufacture automobiles',
                          'lemma': 'plant,works,industrial_plant,'},
             "Synset('plant_n_02')": 
                         {'def': '(botany) a living organism lacking the power of locomotion',
                          'ex': '',
                          'lemma': 'plant,flora,plant_life,'}}
        '''
        return render(request, 'index.html',{
            'dictionary': answers,'search':search
        })
    else:
        return render(request, 'index.html',{
            'dictionary': [],'search':''
        })
