class BruteForceSolution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_of_products = []
        for i in range(len(nums)):
        	tmp = list(nums)
        	del tmp[i]

        	product = 1
        	for num in tmp:
        		product = product * num 
        	list_of_products.append(product)

        return list_of_products

class SolutionWithDivision(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        for i in range(len(nums)):
        	product = product * nums[i]
        products = [product] * len(nums)

        list_of_products = []
        for a, b in zip(products,nums):
        	list_of_products.append(a / b)

        return list_of_products

# Problem asks for a solution in O(n), w/o using division
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        result[0] = 1

        for i in range(1, len(nums)):
        	result[i] = result[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(len(nums))):
        	result[i] *= R
        	R *= nums[i]

        return result
