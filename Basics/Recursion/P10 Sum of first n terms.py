# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

## Problem Description
# Sum of first n terms

class Solution:
    def sumOfSeries(self,n):
        #code here
        # if n<1:
        #     return 0
        
        # return n**3 + self.sumOfSeries(n-1)
        
        sum = (n * (n+1)) // 2
    
        return sum**2
    
# # Example 1:
# Input:
# n=5
# Output:
# 225
# Explanation:
# 13+23+33+43+53=225

# # Example 2:
# Input:
# n=7
# Output:
# 784
# Explanation:
# 13+23+33+43+53+63+73=784