N = int(input())
M = int(input())


def find(a):
    if parent[a] ==a:
        return a
    return find(parent[a])


def union(a,b):
    a = find(a)
    b = find(b)
    
    if a<b:
        parent[a] = b
    else:
        parent[b] = a 
# def find(a):
#     if a == parent[a]:  # 자신이 루트노드면 자신을 반환
#         return a
#     parent[a] = find(parent[a])  # 루트노드를 찾음
#     # 메모이제이션과 비슷한 아이디어
#     # a의 부모를 find(parent[a])로 바꿔줌
#     return parent[a]


# def union(a, b):
#     a = find(a)
#     b = find(b)
#     # a , b의 루트노드를 찾아줌
#     if b < a:
#         parent[a] = b
#     else:
#         parent[b] = a
        
parent = [i for i in range(N + 1)]

# computerGraph = [list(map(int,input().split())) for _ in range(M)]
computerGraph = []
for i in range(M):
    a, b, c = map(int, input().split())
    computerGraph.append((
        a,
        b,
        c,
    ))


computerGraph.sort(key=lambda x: x[2])
res = 0
for a, b,dis in computerGraph:
    if find(a) != find(b):  # 루트가 같으면 할 필요가 없음
        union(a, b)
        res += dis
print(res)


