class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        n=Node(self.head, data)
        self.head = n

    def pop(self):
        if self.head == None:
            raise Exception('Stack Empty')
        val = self.head.data
        self.head = self.head.next
        return val

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def peek(self):
        if self.head == None:
            raise Exception('Stack Empty')
        return self.head.data

    def printstack(self):
        n = self.head
        while n!=None:
            print n.data
            n=n.next


def sortstack(st):
    sttemp = Stack()
    val = st.pop()
    sttemp.push(val)
    while not st.isEmpty():
        val = st.pop()
        num=0
        while sttemp.peek()>val:
            st.push(sttemp.pop())
            num+=1
        sttemp.push(val)
        while num>0:
            sttemp.push(st.pop())
            num-=1
    while not sttemp.isEmpty():
        st.push(sttemp.pop())
    return st




st = Stack()
st.push(1)
st.push(4)
st.push(3)
st.push(0)
st.printstack()
sst = sortstack(st)
sst.printstack()

