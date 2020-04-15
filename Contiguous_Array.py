class BruteForceSolution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0

        for i in range(len(nums)):
            zeros = 0
            ones = 0

            if nums[i] == 0: 
                zeros += 1 
            else:
                ones += 1

            counter = 2 # min possible length is 2
            j = i+1
            while j < len(nums):
                if nums[j] == 0: 
                    zeros += 1 
                else:
                    ones += 1

                if zeros == ones:
                    if counter > max_length:
                        max_length = counter
                counter += 1
                j += 1

        return max_length

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cum_sums = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                cum_sums.append(cum_sums[i] - 1)
            else:
                cum_sums.append(cum_sums[i] + 1)

        lengths = {}
        # lengths = {legnth: (lower, upper)}
        for i in range(len(cum_sums)):
            if cum_sums[i] not in lengths:
                lengths[cum_sums[i]] = [i, None]
            else:
                lengths[cum_sums[i]][1] = i

        max_length = 0
        for k, v in lengths.items():
            if v[1] is not None:
                max_length = max(max_length, v[1] - v[0])

        return max_length
