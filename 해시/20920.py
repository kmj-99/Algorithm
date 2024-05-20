import sys

N,M=map(int,input().rstrip().split())
words = {} # 딕셔너리

for i in range(N):
    word=str(sys.stdin.readline().rstrip())
    if len(word) >= M:
        if word in words:
            words[word]+=1
        else:
            words[word]=1
    else:
        continue
    
words=sorted(words.items() , key = lambda x : (-x[1],-len(x[0]),x[0]))

for i in words:
    print(i[0])
        
        
    