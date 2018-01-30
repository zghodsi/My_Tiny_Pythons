from Queue import *

class Node:
    def __init__(self, num):
        self.adjacent = []
        self.adjcount = 0
        self.visited = False
        self.num = num

    def addadjacent(self, n):
        self.adjacent.append(n)
        self.adjcount+=1


class Graph:
    def __init__(self):
        self.vertices = []
        self.vercount = 0

    def addvertix(self, n):
        self.vertices.append(n)
        self.vercount += 1


    def BFS(self):
        queue = Queue()
        if self.vertices == []:
            raise Exception ('Graph empty')
        queue.put(self.vertices[0])
        while (not queue.empty()):
            n = queue.get()
            if not n.visited:
                n.visited = True
                print n.num 
                for m in n.adjacent:
                    queue.put(m)

        #clean up after search is complete
        for n in self.vertices:
            n.visited = False


    def DFS(self, root):
        n = root
        if n.visited == False:
            n.visited = True
            print n.num
            for m in n.adjacent:
                self.DFS(m)
        

        


if __name__=='__main__':
    G = Graph()
    for i in range (0,6):
        G.addvertix(Node(i))
    G.vertices[0].addadjacent(G.vertices[1])
    G.vertices[0].addadjacent(G.vertices[4])
    G.vertices[0].addadjacent(G.vertices[5])

    G.vertices[1].addadjacent(G.vertices[3])
    G.vertices[1].addadjacent(G.vertices[4])

    G.vertices[2].addadjacent(G.vertices[1])

    G.vertices[3].addadjacent(G.vertices[2])
    G.vertices[3].addadjacent(G.vertices[4])

    print ('BFS:')
    G.BFS()

    print ('DFS:')
    G.DFS(G.vertices[0])
