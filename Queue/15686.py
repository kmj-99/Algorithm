"""

13C6 = 13P6/6! = 400 * 100= 40000 
즉 전수조사로 풀면 된다.

백트랙킹 , BFS , DFS

"""

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int,input().split())) for _ in range(n))

result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chick.append([i,j])

for combi in combinations(chick,m):
    cityValue = 0
    for i in house:
        temp =999
        for j in combi:
            temp=min(abs(i[0]-j[0]) + abs(i[1]-j[1]),temp)
        cityValue+=temp
    result = min(cityValue,result)

print(result)
    
    
            
    

