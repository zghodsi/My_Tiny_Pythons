def modifiedbin(array, item, left, right):
    midindex = (left+right)/2
    if left<=right:
        if item == array[midindex]: 
            return midindex
        if array[left]<array[midindex]:
            if item>=array[left] and item<array[midindex]:  
                return modifiedbin(array, item, left, midindex-1)
            else:
                return modifiedbin(array, item, midindex+1, right)
        else:
            if item>=array[left] or item<array[midindex]:
                return modifiedbin(array, item, left, midindex-1)
            else:
                return modifiedbin(array, item, midindex+1, right)
    return False


array = [15,16,19,20,25,1,3,4,5,7,10,14]
print modifiedbin(array, 1, 0, len(array)-1)
            
            
    
