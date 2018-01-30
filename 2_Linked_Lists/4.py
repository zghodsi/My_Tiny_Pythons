from LinkedList import *

def partition(llist, pivot):
    n = llist.head
    while (n.next!=None):
        if n.next.data<pivot:
            newnode = Node(data=n.next.data, next=llist.head)
            llist.head = newnode
            n.next = n.next.next
        else:
            n = n.next


llist = LinkedList()
llist.addnode(3)
llist.addnode(5)
llist.addnode(8)
llist.addnode(5)
llist.addnode(10)
llist.addnode(2)
llist.addnode(1)
llist.printlist()
partition(llist, 5)
print 'partitioned:'
llist.printlist()
