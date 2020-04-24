class BruteForceSolution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            running_sum = nums[i]

            if running_sum == k:
                counter += 1

            for j in range(i+1, len(nums)):
                running_sum += nums[j]
                if running_sum == k:
                    counter += 1

        return counter

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        previous_sums = {}
        counter = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum == k:
                counter += 1

            if (cur_sum-k) in previous_sums:
                counter += previous_sums[cur_sum-k]

            if cur_sum in previous_sums:
                previous_sums[cur_sum] += 1
            else:
                previous_sums[cur_sum] = 1

        return counter