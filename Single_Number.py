# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Input: [2,2,1]
# Output: 1


class Solution(object):
    def singleNumber(self, numbers):
        numbers.sort()
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                return numbers[i]
            if i % 2 == 0:
                if numbers[i] != numbers[i+1]:
                    return numbers[i]
