# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/selection-sort/1

## Problem Description
# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

class Solution: 
    def select(self, arr, i):
        # code here 
        min = i
        for j in range(i+1, n):
            if arr[j]<arr[min]:
                min = j
        return min
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min = self.select(arr, i)
            arr[i], arr[min] = arr[min], arr[i]

# # Example 1:
# Input:
# N = 5
# arr[] = {4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
# Explanation:
# Maintain sorted (in bold) and unsorted subarrays.
# Select 1. Array becomes 1 4 3 9 7.
# Select 3. Array becomes 1 3 4 9 7.
# Select 4. Array becomes 1 3 4 9 7.
# Select 7. Array becomes 1 3 4 7 9.
# Select 9. Array becomes 1 3 4 7 9.

# # Example 2:
# Input:
# N = 10
# arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10
