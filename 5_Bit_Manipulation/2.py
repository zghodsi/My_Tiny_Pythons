def printbinary(n):
    binlist = []
    for i in range (0,32):
        if n*2>=1:
            binlist.append(1)
            n = 2*n-1
        else:
            binlist.append(0)
            n = 2*n
    if n>0:
        print ('ERROR')
    else:
        print binlist


printbinary(0.72)
