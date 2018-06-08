from nltk.corpus import wordnet as wn
from collections import defaultdict
def OutputSynonym(key):
    ans = {}
    syns = wn.synsets(key, pos='n')
    for s in syns:
        if len(s.lemmas()) <= 1:
            continue
        lemmaList = []
        for l in s.lemmas():
            lemmaList.append(l.name())
        newDict = {}
        newDict['lemma']=lemmaList
        newDict['def']=str(s.definition())
        if s.examples() != []:
            newDict['ex']=str(s.examples()[0])
        else:
            newDict['ex'] = ''
        ans[s.name()]=newDict
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
