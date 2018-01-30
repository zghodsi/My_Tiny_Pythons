def ispath(maze, r, c, path):
    if r<0 or c<0 or not maze[r][c]:
        return False
    isorigin = ((r==0) and (c==0))
    if isorigin or ispath(maze, r-1, c, path) or ispath(maze, r, c-1, path):
        path.append([r, c])
        return True
    return False



def dpispath(maze, r, c, path, failedpoints):
    if r<0 or c<0 or not maze[r][c]:
        return False
    if [r, c] in failedpoints:
        return False
    isorigin = ((r==0) and (c==0))
    if isorigin or dpispath(maze, r-1, c, path, failedpoints) or dpispath(maze, r, c-1, path, failedpoints):
        path.append([r, c])
        return True
    failedpoints.append([r,c])
    return False


def dp(maze, r, c, path):
    failedpoints = []
    return dpispath(maze, r, c, path, failedpoints)
    



maze = [[True]*3 for i in range(3)]
maze[1][1] = False
maze[2][0] = False
path = []
print ispath(maze, 2, 2, path)
print path

otherpath=[]
print dp(maze, 2,2, otherpath)
print otherpath


