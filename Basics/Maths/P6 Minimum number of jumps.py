# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

## Problem Description
""" Given an array of N integers arr[] where each element represents the maximum length of the jump 
that can be made forward from that element. This means if arr[i] = x, then we can jump any distance 
y such that y ≤ x. Find the minimum number of jumps to reach the end of the array (starting from 
the first element). If an element is 0, then you cannot move through that element. Return -1 if you 
can't reach the end of the array.
"""

class Solution:
    def minJumps(self, arr, n):
        #code here
        if len(arr) <= 1:
            return 0
            
        if arr[0] == 0:
            return -1
        
        farthest = 0
        current_end = 0
        jumps = 0
        
        for i in range(n-1):
            farthest = max(farthest, arr[i]+i)
            
            if current_end == i:
                current_end = farthest
                jumps += 1
                
                if current_end >= n-1:
                    return jumps
        return -1
    
# # Example 1:
# Input:
# N = 11 
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
# Output: 3 
# Explanation: 
# First jump from 1st element to 2nd 
# element with value 3. Now, from here 
# we jump to 5th element with value 9, 
# and from here we will jump to the last. 

# # Example 2:
# Input :
# N = 6
# arr = {1, 4, 3, 2, 6, 7}
# Output: 2 
# Explanation: 
# First we jump from the 1st to 2nd element 
# and then jump to the last element.