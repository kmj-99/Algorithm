'''
블로그 포스팅 : X

키워드 : DP

'''

import sys

n = int(sys.stdin.readline())

dp  = [1]*(10)




for i in range(n-1):
    for j in range(1,10):
        dp[j]+=dp[j-1]

print(sum(dp)%10007)


