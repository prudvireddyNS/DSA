# Platform = GFG
# link - https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

# Problem Description
# Given two numbers A and B. The task is to find out their LCM and GCD.

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        
        g = self.gcd(A,B)
        l = A*B//g
        
        return l, g
        
    def gcd(self, A, B):
            if B==0:
                return A
            return self.gcd(B, A%B) 
    
# Example 1:
# Input:
# A = 5 , B = 10
# Output:
# 10 5
# Explanation:
# LCM of 5 and 10 is 10, while
# thier GCD is 5.

# Example 2:
# Input:
# A = 14 , B = 8
# Output:
# 56 2
# Explanation:
# LCM of 14 and 8 is 56, while
# thier GCD is 2.