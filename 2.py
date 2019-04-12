# -*- coding: utf-8 -*-
"""
@author: Trajan
"""

# Calculate the distribution
def get_num(n,f):
    dp = [[0 for i in range(f*n)] for i in range(n)]
    for i in range(f):
        dp[0][i] = 1
    for i in range(1,n):  
        for j in range(i,f*(i+1)):
            add = 0
            for k in range(f):
                add = add + dp[i-1][j-f+k]
            dp[i][j] = add
 
    count = dp[n-1]
    prob = [i/sum(count) for i in count]
    return prob

# Compare the distribution
def compare(Gregor, Oberyn):
    add = 0
    for i in range(1,len(Gregor)):
        add += sum(Oberyn[:i])*Gregor[i]
    return add

if __name__ == "__main__":
    Gregor = get_num(8,5)
    Oberyn = get_num(4,10)
    print("The probability that Gregor wins:", compare(Gregor,Oberyn))