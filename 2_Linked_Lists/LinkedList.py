class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self, head=None):
        self.head=head

    def addnode(self, node_data):
        new_node = Node(node_data)
        if self.head==None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def removenode(self, node_data):
        n = self.head
        if n.data == node_data:
            self.head=n.next
            return

        while (n.next!=None):
            if (n.next.data==node_data):
                n.next = n.next.next
                return
            n = n.next
        
        
    def printlist(self):
        n = self.head
        while (n.next!=None):
            print n.data
            n = n.next
        print n.data


        


def main():
    l = LinkedList()
    l.addnode(5)
    l.addnode(8)
    l.addnode(10)
    l.printlist()

if __name__=="__main__":
    main()
