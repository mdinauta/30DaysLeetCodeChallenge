# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process until the number 
# equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those 
# numbers for which this process ends in 1 are happy numbers.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_of_digits = 0
        seen = []

        while True:
            for digit in str(n):
                sum_of_digits += (int(digit) * int(digit))
            if sum_of_digits == 1:
                return  sum_of_digits
            else:
                n = sum_of_digits
                if n in seen:
                    break
                else:
                    seen.append(n)
                    sum_of_digits = 0

print(Solution().isHappy(19)) 

print(Solution().isHappy(5)) 

