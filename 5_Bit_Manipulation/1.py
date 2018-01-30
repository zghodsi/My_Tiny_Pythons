def insertm(M,N,i,j):
    mask = ~(1<<j-i -1)<<i
    N = N & mask
    return N|(M<<i)


N = 0b100000000000
M = 0b10011
print format(insertm(M,N,2,6), 'b')

