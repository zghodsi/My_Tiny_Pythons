def merge(a,b,sa,sb):
    current = sa+sb-1
    bindex = sb-1
    aindex = sa-1
    while bindex>=0:
        if a[aindex]>b[bindex]:
            a[current] = a[aindex]
            aindex-=1
        else:
            a[current] = b[bindex]
            bindex-=1
        current-=1
    return a
        



a = [1,3,6,0,0]
b = [2,4]
print merge(a,b,3,2)
