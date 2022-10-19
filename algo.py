from collections import deque
import sys

#동 서 남 북
N = int(sys.stdin.readline().strip())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
map = []      
visit = [[0]*N for i in range(N)]
count = 0
for i in range(N):
    input = list(sys.stdin.readline().strip())
    map.append(input)

def dfs(x,y):
    global count
    if x < 0 or x > N-1 or y < 0 or y > N-1: return False 

    visit[x][y] = 1
    print(visit[x][y] == 0)
    print(visit[x][y])
    if map[x][y] == '1' and visit[x][y] == 0:
        count += 1
        for i in range(4):
            dfs(x + dx[i],y + dy[i])
        return True        

    else:
        return False        

result = []

for i in range(N):
    for j in range(N):
        if dfs(i,j):
            result.append(count)
            count = 0
result.sort()
print(len(result))
for i in result:
    print(i)
