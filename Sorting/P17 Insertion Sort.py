# Platform - GFG
# link - https://www.geeksforgeeks.org/problems/insertion-sort/0

## Problem Description
# The task is to complete the insert() function which is used to implement Insertion Sort.

class Solution:
    def insert(self, alist, index, n):
        #code here
        value = alist[index]
        while index>0 and value<alist[index-1]:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = value
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1, n):
            self.insert(alist, i, n)

# # Example 1:
# Input:
# N = 5
# arr[] = { 4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9

# # Example 2:
# Input:
# N = 10
# arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10