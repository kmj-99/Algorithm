'''

주사위를 2차원으로 변환하는 게 핵심!

'''

N,M,x,y,commandNumber = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = []
for i in map(int,input().split()):
    commands.append(i)


dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0,0,0,0,0,0]
# 0 : 위 , 1 : 정면 , 2: 오른 , 3:왼 , 4:뒤 , 5:아래
for command in commands:
    nx=x+dx[command-1]
    ny=y+dy[command-1]
    if 0<=nx<N and 0<=ny<M:
        x=nx
        y=ny
        a,b,c,d,e,f=dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

        if command == 1:
            dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d,b,a,f,e,c
        if command == 2:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
        if command == 3:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
        if command == 4:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


        if board[x][y]==0:
            board[x][y] = dice[5]
        else:
            dice[5]=board[x][y]
            board[x][y] = 0

        print(dice[0])






