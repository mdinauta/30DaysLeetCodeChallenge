class BruteForceSolution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1 

        l = len(nums)
        if l < 4:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1

        mid_point = len(nums) // 2

        # is the first half sorted
        if nums[0] < nums[mid_point]:
            # check if target is in the first half
            if (target >= nums[0]) & (target <= nums[mid_point]):
                for i in range(0, mid_point+1):

                    if nums[i] == target:
                        return i

            else: # check the second half
                for i in range(mid_point, l):
                    if nums[i] == target:
                        return i

        else: # the second half is sorted
            if (target >= nums[mid_point]) & (target <= nums[l-1]):
                for i in range(mid_point, l):
                    if nums[i] == target:
                        return i
            else: 
                for i in range(0, mid_point):
                    if nums[i] == target:
                        return i

        return -1 # target not in the list

class Solution:
    def search(self, nums, target):
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if nums[M] < nums[0] <= target: # +inf
                H = M
            elif nums[M] > nums[0] > target: # -inf
                L = M+1
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1