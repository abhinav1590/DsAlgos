# Program to sort names with similar names
def groupSimilarTitle( t ):
    s = lambda x:[''.join(sorted(x)) if x!= None else None]
    tDict = {}
    l = len(t)
    for i in range(l):
        tList = []
        word = s(t[i])
        for j in range(i,l):
            if t[j] != None and word == s(t[j]):
                tList.append(t[j])
                t[j] = None
        if tList != []:
            tDict[i] = tList

    return tDict

titles = ["spede","duel","dule","speed","deul","cars"]
newList = groupSimilarTitle(titles)
word = 'spede'

for n in newList.values():
    if word in n:
        print(n)
            

