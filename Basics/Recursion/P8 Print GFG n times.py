# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/print-gfg-n-times/1

## Problem Description
# Print GFG n times without the loop.

class Solution:
    def printGfg(self, n):
        # Code here
        if n <1:
            return
        print('GFG', end=' ')
        self.printGfg(n-1)

# # Example:
# Input:
# 5
# Output:
# GFG GFG GFG GFG GFG