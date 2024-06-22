N,S = map(int,input().split(' '))

numbers = list(map(int,input().split(' ')))

cnt =0 
res=[]
def bfs(index):
    global cnt
    if sum(res) == S and len(res)>0:
        cnt+=1
    
    
    for i in range(index,N):
        res.append(numbers[i])
        bfs(i+1)
        res.pop()
bfs(0)
      
print(cnt)