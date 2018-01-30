#mystring = "abcdefabcd"
mystring = "abcdef"

def findunique(mystring):
    #malist = [False for i in range(128)]
    malist = [False]*128
    for i in range (0,len(mystring)):
        val = ord(mystring[i])
        if malist[val]:
            return False
        else:
            malist[val] = True

    return True


print findunique(mystring)

