def lowercase(num):
    if num>=ord('A') and num<=ord('Z'):
        return num-ord('A')+ord('a')
    else:
        return num


def paliper(string):
    malist = [False]*128
    oddnum = 0
    for char in string:
        if char==' ':
            continue
        else:
            if malist[lowercase(ord(char))]==False:
                malist[lowercase(ord(char))] = True
                oddnum+=1
            else:
                malist[lowercase(ord(char))] = False
                oddnum-=1
    if oddnum==1 or oddnum==0:
        return True
    else:
        return False


print paliper('Tac at')
