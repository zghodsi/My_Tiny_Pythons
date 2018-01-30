def binarysearch(array, item):
    left = 0
    right = len(array)-1
    while (left<=right):
        midindex = (right+left)/2
        if item<array[midindex]:
            right = midindex-1
        elif item>array[midindex]:
            left = midindex+1
        else:
            return midindex
    return False



def binarysearchrecuresive(array, item, left, right):
    if (left<=right):
        midindex = (left+right)/2
        if item<array[midindex]:
            return binarysearchrecuresive(array, item, left, midindex-1)
        if item>array[midindex]:
            return binarysearchrecuresive(array, item, midindex+1, right)
        else:
            return midindex
    return False


if __name__=='__main__':
    array = [1,3,5,7,9,11,13,15,17]
    print binarysearch(array, 9)
    print binarysearchrecuresive(array, 6, 0, len(array)-1)
