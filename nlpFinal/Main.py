from nltk.corpus import wordnet as wn
from collections import defaultdict
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11']
final_dict = defaultdict(lambda: list())
result_dict_json_data = os.path.join(BASE_DIR, 'static', "result_2.json")
result_dict_str = open(result_dict_json_data, 'r').read()
result_dict = json.loads(result_dict_str)
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

mostFrequencyDict_json_data = os.path.join(BASE_DIR, 'static', "mostFrequencyDict1.json")
mostFrequencyDict_str = open(mostFrequencyDict_json_data, 'r').read()
mostFrequencyDict = json.loads(mostFrequencyDict_str)

example3Dict_json_data = os.path.join(BASE_DIR, 'static', "Example3.json")
example3Dict_str = open(example3Dict_json_data, 'r').read()
example3Dict = json.loads(example3Dict_str)

def OutputSynonym(key):
    ans = {}
    syns = wn.synsets(key, pos='n')
    for s in syns:
        if len(s.lemmas()) <= 1: continue
        newDict = {}
        sysWord = s.name().split('.')[0]
        if s.name() in mostFrequencyDict:
            newDict['lemma'] = mostFrequencyDict[s.name()]
            newDict['def'] = str(s.definition())
            if s.examples() != []:
                newDict['ex'] = str(s.examples()[0]).replace(sysWord,key)
            else:
                if s.name() in example3Dict:
                    newDict['ex'] = str(example3Dict[s.name()][0]).replace(sysWord,key)
                else:
                    newDict['ex'] = ''
            ans[s.name()] = newDict
    return ans
