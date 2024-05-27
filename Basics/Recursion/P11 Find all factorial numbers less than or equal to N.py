# Platfrom - GFG
# link - 

## Problem Description
# A number N is called a factorial number if it is the factorial of a positive integer. For example,
# the first few factorial numbers are 1, 2, 6, 24, 120. Given a number N, the task is to return the 
# list/vector of the factorial numbers smaller than or equal to N.

class Solution:
    def factorialNumbers(self, N):
        #code here
        self.facts = []
        self.factsBelowN(1)
        return self.facts
    	
    def factsBelowN(self, y):
        if self.fact(y) > N:
            return self.facts
        else:
            self.facts.append(self.fact(y))
            self.factsBelowN(y+1)
    	
    def fact(self, x):
        if x == 1:
            return 1
        return x * self.fact(x-1)
    
# # Example 1:
# Input: N = 3
# Output: 1 2
# Explanation: The first factorial number is 
# 1 which is less than equal to N. The second 
# number is 2 which is less than equal to N,
# but the third factorial number is 6 which 
# is greater than N. So we print only 1 and 2.

# # Example 2:
# Input: N = 6
# Output: 1 2 6
# Explanation: The first three factorial 
# numbers are less than equal to N but 
# the fourth factorial number 24 is 
# greater than N. So we print only first 
# three factorial numbers.
    

    
