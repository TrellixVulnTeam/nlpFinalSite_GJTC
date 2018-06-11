from nltk.corpus import wordnet as wn
from collections import defaultdict
import json

config = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11']
final_dict = defaultdict(lambda: set())
with open('result_2.json') as f:
    result_dict = json.load(f)
for sys in result_dict.keys():
    result = []
    for s in result_dict[sys]:
        if s[0] == 'c7':continue
        temp = []
        for w in s:
            index = w.find('_')
            if index > 0:
                new_w = w[:index] + ' ' + w[index+1:]
                if(new_w.find('_') > -1):continue
                temp.append(new_w)
            else:temp.append(w)
        s = temp
        ss = list(filter(lambda x: x not in config, s))
        result += ss
    final_dict[sys] = list(set(result))

def OutputSynonym(key):
    ans = {}
    syns = wn.synsets(key, pos='n')
    for s in syns:
        if len(s.lemmas()) <= 1:
            continue
        lemmaDict = {}
        l = final_dict[s.name()][0:5]
        i = 5
        for ll in l:
            lemmaDict[ll] = i
            i += 10
        newDict = {}
        newDict['lemma'] = lemmaDict
        newDict['def'] = str(s.definition())
        if s.examples() != []:
            newDict['ex'] = str(s.examples()[0])
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
