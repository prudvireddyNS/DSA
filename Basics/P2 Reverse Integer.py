# Platform - Leetcode
# link - https://leetcode.com/problems/reverse-integer/description/

# Problem Description
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:

        neg = False
        if x<0:
            neg = True

        x = abs(x)
        rev = 0

        while x>0:
            ld = x%10
            rev = rev*10 + ld
            x = x//10

        if neg:
            rev = -rev
               
        if rev<-2**31 or rev>2**31-1:
            return 0
            
        return rev
    
# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21