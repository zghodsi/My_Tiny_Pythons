def isperm_hash(l1,l2):
    if len(l1)!=len(l2):
        return False
    malist = [0 for i in range(128)]
    for item in l1:
        malist[ord(item)]+=1
    for item in l2:
        malist[ord(item)]-=1
        if malist[ord(item)]<0:
            return False
    return True


def isperm(l1,l2):
    l1 = list(l1)
    l2 = list(l2)
    if (len(l1)!=len(l2)):
        return False
    l1.sort()
    l2.sort()
    for i in range (0,len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True


l1 = 'abh'
l2 = 'hab'
print isperm(l1,l2)
print isperm_hash(l1,l2)

