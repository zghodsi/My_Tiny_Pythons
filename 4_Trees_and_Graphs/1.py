from Queue import *

class Node:
    def __init__(self, num):
        self. adjacent=[]
        self.visited = False
        self.num = num

    def addadjacent(self, n):
        self.adjacent.append(n)

class Graph:
    def __init__(self):
        self.vertices = []

    def addvertix(self, n):
        self.vertices.append(n)


    def ispath(self, n, m):
        queue = Queue()
        queue.put(n)
        n.visited = True
        while not queue.empty():
            n = queue.get()
            for r in n.adjacent:
                if r.num == m.num:
                    return True
                if r.visited == False:
                    queue.put(r)
                    r.visited = True
        return False


G = Graph()
for i in range(0,6):
    G.addvertix(Node(i))

G.vertices[0].addadjacent(G.vertices[1])
G.vertices[0].addadjacent(G.vertices[4])
G.vertices[0].addadjacent(G.vertices[5])

G.vertices[1].addadjacent(G.vertices[3])
G.vertices[1].addadjacent(G.vertices[4])

G.vertices[2].addadjacent(G.vertices[1])

G.vertices[3].addadjacent(G.vertices[2])
G.vertices[3].addadjacent(G.vertices[4])

print G.ispath(G.vertices[0],G.vertices[4])

