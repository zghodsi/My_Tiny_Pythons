def repspace(string, l):
    numspace=0
    for i in range (0,l):
        if string[i]==' ':
            numspace+=1
    tl = l+numspace*2
    print tl
    for i in range(0,l):
        if string[i]==' ':
            string = string[:i]+'%20'+string[i+1:tl-2]
    return string


string = 'Mr John Smith      '
print repspace(string, 13)

