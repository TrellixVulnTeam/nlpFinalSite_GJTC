from nltk.corpus import wordnet as wn
from collections import defaultdict
def OutputSynonym(key):
    ans = {}
    syns = wn.synsets(key, pos='n')
    for s in syns:
        if len(s.lemmas()) <= 1:
            continue
        string = ''
        for l in s.lemmas():
            string += l.name()
            string += ','
        key = str(s).replace('.', '_')
        newDict = {}
        newDict['lemma']=string
        newDict['def']=str(s.definition())
        if s.examples() != []:
            newDict['ex']=str(s.examples()[0])
        else:
            newDict['ex'] = ''
        ans[key]=newDict
    return ans

'''
def OutputSynonym(key):
    ans = []
    syns = wn.synsets(key, pos='n')
    for s in syns:
        if len(s.lemmas()) <= 1:
            continue
        ans.append(s)
        for l in s.lemmas():
            ans.append(l.name())
        ans.append(s.definition())
        ans.append(s.examples())
    return ans
'''
