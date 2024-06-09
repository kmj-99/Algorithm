

'''
 키워드 : dfs를 적용하여 문제를 품

배운 점 : sys.setrecursionlimit(10**4)를 이용해겨 재귀깊이를 설정할 수 있다. 
    하지만 문제는 수치를 높게 설정하면 메모리도 같이 잡아먹기에 메모리 초과가 뜰 수 있다는 점을 주의해야한다. 
'''



import sys
import copy

n=int(input())

sys.setrecursionlimit(10**4)

graph=[]
colorWeaknessGraph=[]

for i in range(n):
    graph.append(list(map(str,input())))


colorWeaknessGraph=copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if colorWeaknessGraph[i][j]=="R":
            colorWeaknessGraph[i][j]="G"

def dfs(i,j,target):
    
    if i<0 or i>=n or j<0 or j>=n:
        return False

    if graph[i][j]==target:
        graph[i][j]="V"
        dfs(i-1,j,target)
        dfs(i+1,j,target)
        dfs(i,j-1,target)
        dfs(i,j+1,target)
    
    return True

def colorWeaknessDfs(i,j,target):

    if i<0 or i>=n or j<0 or j>=n:
        return False

    if colorWeaknessGraph[i][j]==target:
        colorWeaknessGraph[i][j]="V"
        colorWeaknessDfs(i-1,j,target)
        colorWeaknessDfs(i+1,j,target)
        colorWeaknessDfs(i,j-1,target)
        colorWeaknessDfs(i,j+1,target)
    return True


res=0
colorWeaknessRes=0
for i in range(n):
    for j in range(n):
        if graph[i][j]!="V":
            dfs(i,j,graph[i][j])
            res+=1
        if colorWeaknessGraph[i][j]!="V":
            colorWeaknessDfs(i,j,colorWeaknessGraph[i][j])
            colorWeaknessRes+=1
print(res,end=' ')

print(colorWeaknessRes)

