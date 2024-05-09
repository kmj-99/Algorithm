



def dfs():
    if(len(arr) == M):
        print(' '.join(map(str,arr)))
        return 
    else:
        for i in range(1,N+1):
            if not visited[i]:
                visited[i]=True
                arr.append(i)
                dfs()
                arr.pop()
                visited[i]=False
                

            






N,M=map(int,input().split(' '))
visited = [False]*(N+1)
arr = []
dfs()
