# Platform - GFG
# link - 

## Problem Description
# Print N to 1 without loop

class Solution:
    def printNos(self, n):
        # Code here
        if n < 1:
            return 
        print(n, end=' ')
        self.printNos(n-1)

# # Example 1:
# Input:
# N = 10
# Output: 10 9 8 7 6 5 4 3 2 1