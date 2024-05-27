# Platform - Leetcode
# link - https://leetcode.com/problems/valid-palindrome/description/

## Problem Description
""" A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward 
and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""

# without recursion
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]','', s)
        rev = s[::-1]
        return s==rev
    
# Using recursion
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]','', s)
        return self.pal(s,0)
        
    def pal(self, s, i):
        if i>=len(s)/2:
            return True
        if s[i] != s[len(s)-i-1]:
            return False
        # print(s[i], s[len(s)-i-1])
        # print(i, len(s)/2)
        return self.pal(s,i+1)

# # Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# # Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# # Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
        
