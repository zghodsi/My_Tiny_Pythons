class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.min = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node()
            self.head.value = value
            self.head.min = value
        else:
            n = Node()
            n.next = self.head
            n.value = value
            n.min = min(value, self.head.min)
            self.head = n

    def pop (self):
        if self.head == None:
            raise Exception('Stack Empty')
        val = self.head.value
        self.head = self.head.next
        return val

    def min(self):
        return self.head.min


st = Stack()
st.push(5)
print st.min()
st.push(4)
print st.min()
st.push(3)
print st.min()
st.pop()
st.pop()
print st.min()
