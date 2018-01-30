from LinkedList import LinkedList       

def removedup(l):
    mylist = [False]*128
    n = l.head
    mylist[ord(n.data)]=True
    while (n.next!=None):
        if mylist[ord(n.next.data)]==False:
            mylist[ord(n.next.data)]=True
            n = n.next
        else:
            n.next = n.next.next



def followup(l):
    n1 = l.head
    while (n1!=None):
        n2=n1
        while (n2.next!=None):
            if n2.next.data == n1.data:
                n2.next=n2.next.next
            else:
                n2 = n2.next
        n1=n1.next



l = LinkedList()
l.addnode('b')
l.addnode('b')
l.addnode('d')
l.addnode('b')
l.addnode('c')
l.addnode('d')
l.addnode('e')
l.addnode('e')
l.printlist()
print('now removing dups:')
#removedup(l)
followup(l)
l.printlist()


