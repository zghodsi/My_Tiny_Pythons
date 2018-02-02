class Listy:
    def __init__(self, array):
        self.array = array
        self.len = len(array)

    def elementAt(self,i):
        if i>self.len:
            return -1
        return self.array[i]




def sortedsearch(mylisty, x, left, right):
    if right<left:
        return -1

    mid = (left+right)/2
    miditem = mylisty.elementAt(mid)

    if miditem==x:
        return mid

    if miditem==-1 or miditem>x:
        return sortedsearch(mylisty, x, left, mid-1)
    elif mylisty.elementAt(right)==-1:
        return sortedsearch(mylisty, x, mid+1, right)
    else:
        return sortedsearch(mylisty, x, mid+1, 2*right)
        
    

mylisty = Listy([2, 5, 8, 12, 34, 74, 92])
print sortedsearch(mylisty, 12, 0, 2)
