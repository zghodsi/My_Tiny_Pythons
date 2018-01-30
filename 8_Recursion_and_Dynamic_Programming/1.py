def triplestep(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return triplestep(n-1)+triplestep(n-2)+triplestep(n-3)


def ts(n, mem):
    if n==1:
        mem[0] = 1
    elif n==2:
        mem[1] = 2
    elif n==3:
        mem[2] = 4

    elif mem[n-1]==0:
        mem[n-1] = ts(n-1, mem) + ts(n-2, mem) + ts(n-3, mem) 
    return mem[n-1]

def triplestepmem(n):
    mem = [0]*n
    return ts(n, mem)
    

for i in range (1,6):
    print triplestep(i)
    print triplestepmem(i)
