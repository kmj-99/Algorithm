import sys
from queue import PriorityQueue
N = int(sys.stdin.readline().rstrip())

homeworks = []
queue = PriorityQueue()

for i in range(N):
    homeworks.append(list(map(int,sys.stdin.readline().split(" "))))


    

