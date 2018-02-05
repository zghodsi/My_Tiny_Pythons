def findstring(mystring, array, left, right):
    mid = (left+right)/2
    if mystring==array[mid]:
        return mid
    elif left<right:
        if array[mid]=='':
            while left<=mid and array[mid]=='':
                mid-=1
            if mystring==array[mid]:
                return mid
            if mystring>array[mid] or left==mid:
                return findstring(mystring, array, mid+1, right)
            else:
                return findstring(mystring, array, left, mid-1)
    return -1

array = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dog', '', '']
print findstring('dog', array, 0, len(array))
