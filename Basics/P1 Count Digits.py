# Platform - GFG
# https://www.geeksforgeeks.org/problems/count-digits5716/1

# Problem Description - 
# Given a number N. Count the number of digits in N which evenly divide N.

class Solution:
    def evenlyDivides (self, N):
        # code here
        temp = N
        cnt = 0
        while N>0:
            # print(N)
            ld = N%10
            if ld>0 and temp%ld==0:
                cnt += 1
            N =  N // 10
        return cnt
    
# Example 1:

# Input:
# N = 12
# Output:
# 2
# Explanation:
# 1, 2 both divide 12 evenly
# Example 2:

# Input:
# N = 23
# Output
# 0
# Explanation:
# 2 and 3, none of them
# divide 23 evenly