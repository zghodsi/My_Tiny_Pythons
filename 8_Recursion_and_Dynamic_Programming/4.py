def getsuperset(myset):
    superset=[]
    if len(myset)==1:
        superset.append([])
        superset.append(myset)
        return superset

    firstitem = myset[0]
    partition = myset[1:]
    partsuperset = getsuperset(partition)
    #print 'superset: ',partsuperset
    for item in partsuperset:
        auxitem = list(item)

        item.append(firstitem)

        superset.append(auxitem)
        superset.append(item)
        #print superset

    return superset


print getsuperset([1,2,3])
        
