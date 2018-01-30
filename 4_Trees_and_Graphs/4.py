class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


def getheight(treenode):
    if treenode==None:
        return -1
    leftheight = getheight(treenode.left)
    rightheight = getheight(treenode.right)

    if leftheight == -2 or rightheight == -2:
        return -2

    if abs(leftheight - rightheight)>1:
        return -2

    return max(leftheight, rightheight)+1


root = Node(8)
root.left= Node(4)
root.left.left = Node(2)
print getheight(root)

