
'''

키워드 : 백트랙킹을 활용하여 bfs를 적용해 접근

해당 문제 리마인드 하기

리마인드 횟수 : 0 
'''



from collections import deque
import copy

# 세로크기 n , 가로크기 m
n,m= map(int,input().split())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))



def bfs():
    queue=deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
             if tmp_graph[i][j]==2:
                queue.append((i,j))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if tmp_graph[nx][ny]==0:
                tmp_graph[nx][ny]=2
                queue.append((nx,ny))
    global answer
    cnt=0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer=max(cnt,answer)


def backTrackingWall(wallCount):
    if wallCount==3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                backTrackingWall(wallCount+1)
                graph[i][j]=0
answer=0
backTrackingWall(0)
print(answer)
