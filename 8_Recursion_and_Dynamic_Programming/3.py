def mindex(array, index):
    if len(array)==0:
        return -1
    midi = (len(array))/2
    if array[midi]==index[midi]:
        return index[midi]
    if array[midi]>index[midi]:
        return mindex(array[:midi], index[:midi])
    if array[midi]<index[midi]:
        return mindex(array[midi+1:], index[midi+1:])
    return -1


def magicindex(array):
    index = [i for i in range(len(array))]
    return mindex(array, index)


array = [-1, 0, 3, 4, 5 , 8]
print magicindex(array)
