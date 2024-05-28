## Platform - GFG
# link - https://www.geeksforgeeks.org/problems/bubble-sort/1

## Problem Description
# Given an Integer N and a list arr. Sort the array using bubble sort algorithm.

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n-1):
            didSwap = 0
            for j in range(n-i-1):
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    didSwap = 1
            if didSwap == 0:
                break
    
# # Example 1:
# Input: 
# N = 5
# arr[] = {4, 1, 3, 9, 7}
# Output: 
# 1 3 4 7 9

# # Example 2:
# Input:
# N = 10 
# arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output: 
# 1 2 3 4 5 6 7 8 9 10