# for next bigger, find the first 01 from right and turn to 10
# for next smaller, find the first 10 from right and turn to 01


def seti(num, i):
    mask = 1<<i
    return num|mask

def reseti(num, i):
    mask = ~(1<<i)
    return num&mask

#FIXME upperbound on current
def nextnum(number):
    num = number
    current = 0
    lsb = num & 1
    if lsb:
        while lsb:
            current+=1
            if current>32:
                return -1,-1
            num = num>>1
            lsb = num&1
        nextbigger = reseti(seti(number, current), current-1)
        
        while not lsb:
            current+=1
            if current>32:
                return -1,nextbigger
            num=num>>1
            lsb = num&1
        nextsmaller = reseti(seti(number, current-1), current)

    if not lsb:
        while not lsb:
            current+=1
            if current>32:
                return -1,-1
            num=num>>1
            lsb = num&1
        nextsmaller = reseti(seti(number, current-1), current)
        
        while lsb:
            current+=1
            if current>32:
                return nextsmaller, -1
            num = num>>1
            lsb = num&1
        nextbigger = reseti(seti(number, current), current-1)

    return nextsmaller, nextbigger


print nextnum(6)
        

