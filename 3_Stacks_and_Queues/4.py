class Node:
    def __init__(self):
        self.value = None
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,value):
        n = Node()
        n.value = value
        n.next = self.head
        self.head = n

    def pop(self):
        if self.head == None:
            raise Exception('Stack Empty')
        val = self.head.value
        self.head = self.head.next
        return val

    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def printstack(self):
        n = self.head
        if n==None:
            return
        while n.next!=None:
            print n.value
            n = n.next
        print n.value


class MyQueue:
    def __init__(self):
        self.inorder = Stack()
        self.reverse = Stack()

    def add(self, item):
        if self.inorder.empty():
            while not self.reverse.empty():
                self.inorder.push(self.reverse.pop())
        self.inorder.push(item)

    def remove(self):
        if self.reverse.empty():
            while not self.inorder.empty():
                self.reverse.push(self.inorder.pop())
        return self.reverse.pop()

    def printqueue(self):
        self.inorder.printstack()
        self.reverse.printstack()


if __name__=='__main__':
    myqueue = MyQueue()
    myqueue.add(1)
    myqueue.add(3)
    myqueue.add(5)
    myqueue.add(6)
    myqueue.add(9)
    myqueue.printqueue()
    myqueue.remove()
    myqueue.remove()
    print 'after remove:'
    myqueue.add(2)
    myqueue.printqueue()
