class Node:
    def __init__(self):
        self.value = None
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.nextstack = None
        self.size = 0

    def push(self,value):
        n = Node()
        n.value = value
        n.next = self.head
        self.head = n
        self.size+=1

    def pop(self):
        if self.head == None:
            raise Exception('Stack Empty')
        val = self.head.value
        self.head = self.head.next
        self.size-=1
        return val



class SetOfStacks:
    def __init__(self):
        self.stackhead = None
        self.th = 3
        self.size = 0
    
    def push(self, value):
        if self.stackhead and self.stackhead.size < self.th:
            self.stackhead.push(value)
        else:
            s = Stack()
            s.nextstack = self.stackhead
            self.stackhead = s
            self.stackhead.push(value)
            self.size+=1
    
    def pop(self):
        val = self.stackhead.pop()
        if self.stackhead.size == 0:
            self.stackhead = self.stackhead.nextstack
        return val

    def popat(self, index):
        i = self.size - index
        n = self.stackhead
        while i!=0:
            n = n.nextstack
            i-=1
        return n.pop()



sst = SetOfStacks()
sst.push(5)
sst.push(4)
sst.push(3)
sst.push(2)
sst.push(1)
sst.push(0)
print sst.pop()
print sst.popat(1)
