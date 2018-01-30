def groupanagrams(array):
    anagramdict = {}
    for string in array:
        k = ''.join(sorted(string))
        if k in anagramdict:
            anagramdict[k].append(string)
        else:
            anagramdict[k]=[]
            anagramdict[k].append(string)

    anagramarray=[]
    for key in anagramdict:
        for val in anagramdict[key]:
            anagramarray.append(val)
    return anagramarray



array = ['cat', 'dog', 'horse', 'god', 'act', 'odg']
print groupanagrams(array)
