from LinkedList import LinkedList


def delmiddle(node):
    node.data = node.next.data
    node.next=node.next.next


l = LinkedList()
l.addnode(1)
l.addnode(2)
l.addnode(3)
l.addnode(4)
l.addnode(5)
l.printlist()
node = l.head.next
print 'removing middle:'
delmiddle(node)
l.printlist()

