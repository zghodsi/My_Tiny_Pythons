class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

def mintree(array):
    if len(array)==0:
        return None
    else:
        n = Node()
        s = len(array)-1
        rootindex = s/2
        n.val = array[rootindex]
        print array
        print 'root:'+ str(n.val)
        n.left = mintree(array[:s/2])
        n.right = mintree(array[s/2+1:])
        return n


def printtree(root):
    if (root!=None):
        print root.val
        printtree(root.left)
        printtree(root.right)
    else:
        return

array = [1, 2, 3, 4, 5, 6]
root = mintree(array)
printtree(root) 
