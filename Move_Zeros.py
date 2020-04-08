# Given an array nums, write a function to move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


class BruteForceSolution(object):
    def moveZeroes(self, nums):
        """
        type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place
        """
        new_nums = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                new_nums.append(nums[i])
        
        for _ in range(zero_count):
            new_nums.append(0)

        return new_nums

# Solve without making a copy of the array
class Solution(object):
    def moveZeroes(self, nums):
        """
        type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        
        return nums

class testSolution(object):
    def testMoveZeros(self):
        solution = Solution()

        nums = [0,1,0,3,12]
        result = solution.moveZeroes(nums)
        print(result)

        nums = [0]
        result = Solution().moveZeroes(nums)
        print(result)
        
        nums = [1,2,3]
        result = Solution().moveZeroes(nums)
        print(result)

        nums = [0,0,1]
        result = Solution().moveZeroes(nums)
        print(result)


# testSolution().testMoveZeros()
