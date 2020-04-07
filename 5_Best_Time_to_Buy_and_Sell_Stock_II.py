# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
        	profit += max(prices[i] - prices[i-1], 0)

        return profit

class TestSolution(object):
	def testMaxProfile(self):
		solution = Solution()

		prices = [7,1,5,3,6,4]
		result = solution.maxProfit(prices)
		print('Prices: ', prices)
		print('Result: ', result)
		print('Correct result: ', 7)

		prices = [1,2,3,4,5]
		result = solution.maxProfit(prices)
		print('Prices: ', prices)
		print('Result: ', result)
		print('Correct result: ', 4)

		prices = [7,6,4,3,1]
		result = solution.maxProfit(prices)
		print('Prices: ', prices)
		print('Result: ', result)
		print('Correct result: ', 0)

# TestSolution().testMaxProfile()
