# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/merge-sort/1

## Problem Description
# Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        temp = []
        i = l
        j = m+1
        while i<=m and j<=r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= m:
            temp.append(arr[i])
            i += 1
        while j <= r:
            temp.append(arr[j])
            j += 1
        for i in range(l, r+1):
            arr[i] = temp[i - l]
                        
    def mergeSort(self,arr, l, r):
        #code here
        if l<r:
            mid = (l+r)//2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)

# Example 1:
# Input:
# N = 5
# arr[] = {4 1 3 9 7}
# Output:
# 1 3 4 7 9

# Example 2:
# Input:
# N = 10
# arr[] = {10 9 8 7 6 5 4 3 2 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10
