from Queue import *

class TNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class LLNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self,item):
        if self.root == None:
            self.root=LLNode(item)
        else:
            n = LLNode(item)
            n.next = self.root
            self.root = n

    def printlinkedlist(self):
        if self.root == None:
            print 'linked list empty'
            return
        print 'linked list:'
        n = self.root
        while n!=None:
            print n.val
            n = n.next


def lldepth(root):
    linkedlistlist = []
    thislevel = Queue()

    thislevel.put(root)
    while not thislevel.empty():
        l = LinkedList()
        qs = thislevel.qsize()
        for i in range (0, qs):
            n = thislevel.get()
            l.insert(n.val)
            print n.val
            if n.left!=None:
                thislevel.put(n.left)
            if n.right!=None:
                thislevel.put(n.right)
        linkedlistlist.append(l)

    return linkedlistlist


if __name__=='__main__':
    root = TNode(1)
    root.left = TNode(2)
    root.right = TNode(3)
    root.left.left = TNode(4)
    root.left.right = TNode(5)
    root.right.right = TNode(6)
    root.right.right.left = TNode(7)
    lllist = lldepth(root)
    for i in lllist:
        i.printlinkedlist()  
    


