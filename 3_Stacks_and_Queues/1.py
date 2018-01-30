class TriStack:
    def __init__(self):
        self.stacksize = 4
        self.array = [0]*self.stacksize*3
        self.sizes = [0]*3

    def push (self, stacknum, value):
        if (self.sizes[stacknum-1]==self.stacksize):
            raise Exception('Stack Full')

        self.array[self.stacksize*(stacknum-1)+self.sizes[stacknum-1]] = value
        self.sizes[stacknum-1]+=1


    def pop (self, stacknum):
        if (self.sizes[stacknum-1]==0):
            raise Exception('Stack Empty')

        self.sizes[stacknum-1]-=1
        return self.array[self.stacksize*(stacknum-1)+self.sizes[stacknum-1]]


ts = TriStack()
ts.push(1,5)
ts.push(1,4)
ts.push(1,3)
ts.push(1,2)
print ts.pop(1)
print ts.pop(1)
print ts.pop(1)


