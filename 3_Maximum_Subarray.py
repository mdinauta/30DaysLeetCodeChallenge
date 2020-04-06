# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class BruteForceSolution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for i in range(len(nums)):

            if nums[i] > max_sum:
                max_sum = nums[i]
            if i+1 == len(nums):
                break
            
            j = i+1
            curr_sum = nums[i]

            while j < len(nums):
                n = nums[j]
                curr_sum += n
                if curr_sum > max_sum:
                    max_sum = curr_sum
                j += 1
        
        return max_sum

# Kadane's algorithm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            cur_sum = max(n, cur_sum+n)
            max_sum = max(cur_sum, max_sum)
        return max_sum

# Kadane's algorithm
class SolutionIllustration(object):
    def maxSubArray(self, nums):
        """
        Includes print states to better understand the algo
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            print('cur_sum: ', cur_sum)
            print('max_sum: ', max_sum)
            print('which is greater ', n, 'or ', cur_sum+n)
            cur_sum = max(n, cur_sum+n)
            print('new cur_sum: ', cur_sum)
            print('which is greater ', cur_sum, 'or ', max_sum)
            max_sum = max(cur_sum, max_sum)
            print('new max_sum: ', max_sum)
            print('\n')
        return max_sum



test_str = [-2,1,-3,4,-1,2,1,-5,4]
# test_str = [-1]
# test_str = [2]
print(Solution().maxSubArray(test_str))
