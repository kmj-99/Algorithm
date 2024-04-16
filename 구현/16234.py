'''
bfs로 국경선을 열 수 있는 국가의 수를 구함 -> 구한 국가는 list에 저장 -> list에서 갱신값 구해서 국가 인구수 갱신

3 5 10
10 15 20
20 30 25
40 22 10

10 15 20
20 30 25
40 22 10
'''
from collections import deque

N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union      

result=0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0 
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                visited[i][j]=1
                country=bfs(i,j)

                if len(country)>1:
                    flag=1
                    people = sum(A[x][y] for x, y in country) // len(country)
                    for x,y in country:
                        A[x][y]=people

        
    if flag == 0:
        print(result)
        break

    result += 1
