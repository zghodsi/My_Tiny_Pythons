class MinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.heapsize = 0

    def bubbleup(self, c, value):
        p = c/2
        while (p>0):
            if self.heaplist[p]>value:
                #swap
                self.heaplist[c] = self.heaplist[p]
                self.heaplist[p] = value
            c = p
            p = p/2


    def bubbledown(self, p):
        while (2*p<self.heapsize):
            if self.heaplist[2*p]>self.heaplist[2*p+1]:
                c = 2*p+1
            else:
                c = 2*p

            tmp = self.heaplist[p]
            self.heaplist[p] = self.heaplist[c]
            self.heaplist[c] = tmp
            p = c


    def insert(self, value):
        self.heaplist.append(value)
        self.heapsize+=1
        self.bubbleup(self.heapsize,value)


    def extractmin(self):
        minval = self.heaplist[1]
        lastval = self.heaplist[self.heapsize]
        self.heaplist = self.heaplist[:self.heapsize]
        self.heaplist[1] = lastval
        self.heapsize-=1
        self.bubbledown(1)


    def printheap(self):
        print self.heaplist



if __name__=='__main__':
    mh = MinHeap()
    mh.insert(5)
    mh.insert(4)
    mh.insert(1)
    mh.insert(2)
    mh.insert(0)
    mh.printheap()
    mh.extractmin()
    print('after')
    mh.printheap()
    mh.insert(3)
    print('after')
    mh.printheap()
