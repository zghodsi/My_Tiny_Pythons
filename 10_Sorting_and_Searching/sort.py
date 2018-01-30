#bubble sort
def bubblesort(array):
    for i in range (0,len(array)):
        for j in range (0, len(array)-i-1):
            if array[j]>array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
    return array

#selection sort
def selectionsort(array):
    for i in range (0, len(array)):
        minval=array[i]
        minindex=i
        for j in range (i+1, len(array)):
            if array[j]<minval:
                minval = array[j]
                minindex = j
        tmp = array[i]
        array[i] = array[minindex]
        array[minindex] = tmp
    return array


#merge sort
def merge(array, left, mid, right):
    helperarray = array[left:right+1]
    index1=0
    index2=mid-left

    current=left

    while(index1<mid-left and index2<right-left+1):
        if helperarray[index1]<helperarray[index2]:
            array[current] = helperarray[index1]
            index1+=1
        else:
            array[current] = helperarray[index2]
            index2+=1
        current+=1

    while index1<mid-left:
        array[current] = helperarray[index1]
        current+=1
        index1+=1

def mergesort(array, left, right):
    if right-left<1:
        return
    mid = (left+right)/2
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge(array, left, mid+1, right)
    return array


#quick sort
def quicksort(array, left, right):
    index = partition(array, left, right)
    if left<index-1:
        quicksort(array, left, index-1)
    if right>index:
        quicksort(array, index, right)
    return array

def partition(array, left, right):
    mid = (left+right)/2
    while (left<=right):
        while array[left]<array[mid]:
            left+=1
        while array[right]>array[mid]:
            right-=1

        if left<=right:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            left+=1
            right-=1
    return left

array = [7,3,5,1,9,3,0]
print array
print bubblesort(array[:])
print selectionsort(array[:])
print mergesort(array[:], 0, len(array)-1)
print quicksort(array[:], 0, len(array)-1)
