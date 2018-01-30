def oneaway(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    if abs(len(s1)-len(s2))>1:
        return False
    p1 = 0
    p2 = 0

    seen=False

    while p1<len(s1) and p2<len(s2):
        if s1[p1]==s2[p2]:
            p1+=1
            p2+=1
        elif p1+1>=len(s1) or p2+1>=len(s2):
            break
        elif s1[p1]==s2[p2+1]:  
            if seen:
                return False
            seen = True
            p2+=1
        elif s1[p1+1]==s2[p2]:
            if seen:
                return False
            seen = True
            p1+=1
        elif s1[p1+1]==s2[p2+1]:
            if seen:
                return False
            seen = True
            p1+=1
            p2+=1
        else:
            return False

    return True


print oneaway('pale', 'ple')
print oneaway('pale', 'pala')
print oneaway('bake', 'pale')

