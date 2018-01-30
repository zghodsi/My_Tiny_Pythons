from LinkedList import *

def sumlists(num1, num2):
    carry = 0
    n1 = num1.head
    n2 = num2.head
    result = LinkedList()
    while n1.next!=None and n2.next!=None:
        result.addnode((carry+n1.data+n2.data)%10)
        carry = (carry+n1.data+n2.data)/10
        n1 = n1.next
        n2 = n2.next

    result.addnode((carry+n1.data+n2.data)%10)
    carry = (carry+n1.data+n2.data)/10

    if n1.next==None:
        n = n2.next
    else:
        n = n1.next

    while n!=None:
        result.addnode((carry+n.data)%10)
        carry = (carry+n.data)/10
        n = n.next

    if carry!=0:
        result.addnode(carry)

    return result


num1 = LinkedList()
num1.addnode(1)
num1.addnode(7)
num2 = LinkedList()
num2.addnode(2)
num2.addnode(9)
num2.addnode(5)
result = sumlists(num1, num2)
result.printlist()

