from LinkedList import LinkedList

def findk(l,k):
    n1 = l.head
    n2 = l.head
    i=k

    while (n1.next!=None):
        if i>0:
            n1 = n1.next
            i-=1
        else:
            n1=n1.next
            n2=n2.next

    return n2.data


l = LinkedList()
l.addnode(1)
l.addnode(2)
l.addnode(3)
l.addnode(4)
l.addnode(5)
l.printlist()

k = 7
print str(k) + ' : ' + str(findk(l,k))


