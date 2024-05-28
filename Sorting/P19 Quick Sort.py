# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/quick-sort/1

## Problem Description
# Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
# Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
    
    def partition(self,arr,low,high):
        # code here
        p = arr[high]
        i = low-1
        for j in range(low, high):
            if arr[j] < p:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
                
# Example 1:
# Input: 
# N = 5 
# arr[] = { 4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9

# Example 2:
# Input: 
# N = 9
# arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
# Output:
# 1 1 2 3 4 6 7 9 10