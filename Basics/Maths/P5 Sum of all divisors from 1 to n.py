# Platform - GFG
# link = https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1

## Problem Description
# Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) 
# for the number i is defined as the sum of all divisors of i.

class Solution:
    def sumOfDivisors(self, N):
        #code here 
        #     tot_sum = 0
        #     for i in range(1, N+1):
        #         sum = 0
        #         for j in range(1, int(i**0.5)+1):
        #             if i%j==0:
        #                 sum += j
        #                 if i/j != j:
        #                     sum += i/j
        #         tot_sum += sum
        #     return int(tot_sum)
        
        sum = 0
        for i in range(1, N+1):
            sum += i*(N//i)  # ⌊N//i⌋ gives the count of numbers between 1 and 𝑁 that are divisible by i

## Example 1:
# Input:
# N = 4
# Output:
# 15
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# ans = F(1) + F(2) + F(3) + F(4)
#     = 1 + 3 + 4 + 7
#     = 15

## Example 2:
# Input:
# N = 5
# Output:
# 21
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# F(5) = 1 + 5 = 6
# ans = F(1) + F(2) + F(3) + F(4) + F(5)
#     = 1 + 3 + 4 + 7 + 6
#     = 21