from queue import PriorityQueue
import sys



N = int(sys.stdin.readline().rstrip())

queue = PriorityQueue()


for i in range(N):
    num = int(sys.stdin.readline().rstrip())

    if num==0:
        if queue.empty():
            print(0)
        else:
            print(queue.get())
    else:
        queue.put(num)
    
        

    