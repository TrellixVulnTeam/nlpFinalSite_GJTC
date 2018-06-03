from nltk.corpus import wordnet as wn
def Cal(key):
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
