import sys
from collections import deque

input = sys.stdin.readline

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
x,y,size = 0,0,2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def bfs(x,y,size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x,y))
    temp = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                if graph[nx][ny] <= size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y]+1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))

                    

                
    
res = 0

while 1:
    shark = bfs(x,y,size)
    if len(shark)==0:
        break
    nx,ny,dist = shark.pop()
    res+=dist
    graph[x][y],graph[nx][ny] = 0,0
    x,y=nx,ny
    cnt+1
    if cnt==size:
        cnt=0
        size+=1
print(res)


