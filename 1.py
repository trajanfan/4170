# -*- coding: utf-8 -*-
"""
@author: Trajan
"""

def make_currency(a, total):
    if len(a) <= 1:
        return 1
    dp = [[0 for i in range(len(a))] for i in range(total+1)]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(len(dp[0])):
        dp[0][i] = 1
    for i in range(1,len(dp[0])):
        for j in range(1,len(dp)):
            if j>=a[i]:
                add = dp[j - a[i]][i]
            else:
                add = 0
            dp[j][i] = dp[j][i-1] + add
    return dp[total][len(a)-1]

if __name__ == "__main__":
#    import time
#    start = time.time()
    print("The number of ways is:",make_currency([1,5,10,20,50,100],500))
#    end = time.time()
#    print("Run time: ",end-start)
