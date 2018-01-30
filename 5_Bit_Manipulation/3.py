def flip(n):
    currentcount = 0
    prevcount = 0

    prevbit = 0
    maxseq = 0

    while n!=0:
        if n%2 == 1:
            currentcount+=1
            prevbit = 1
        else:
            maxseq = max(currentcount+prevcount+1, maxseq)
            if prevbit == 1:
                prevcount = currentcount
                currentcount = 0
            else:
                prevcount = 0
            prevbit = 0

        n = n>>1

    maxseq = max(currentcount+prevcount+1, maxseq)
    return maxseq
            

print flip(0b11011101111)
print flip(0b1111110011101011)
