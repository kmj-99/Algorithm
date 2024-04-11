'''
1번 주사위만 픽스되면 나머지 주사위위치는 알아서 픽스된다.
1번 주사위 위치를 모두 비교해 가면서 가장 합이 높은 수를 추출하면 된다.

A, B, C, D, E, F

A - F 
B - D
C - E
'''
across_dict = {
  0 : 5,
  1 : 3,
  2 : 4,
  3 : 1,
  4 : 2,
  5 : 0
}

diceNumber = int(input())

dice = [list(map(int,input().split())) for _ in range(diceNumber)]


res=0
resList=[]
for i in range(6):
    underSide = dice[0][i]
    res=0
    for j in range(0,diceNumber):
        for k in range(6):
            if underSide == dice[j][k]:
                across_num = dice[j][across_dict[k]]
                if 6 in [underSide,across_num]:
                    res +=4 if 5 in [underSide,across_num] else 5
                else:
                    res +=6
                underSide=across_num
                break
        
    resList.append(res)


print(max(resList))