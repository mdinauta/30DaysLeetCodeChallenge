class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_hash = {}
        for n in arr:
        	arr_hash[n] = None

        count = 0
        for i in range(len(arr)):
        	if arr[i]+1 in arr_hash:
        		count += 1 

        return count

class TestSolution(object):
    def test_CountElements(self):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solution = Solution()
        arr = [1,2,3]
        result = solution.countElements(arr)
        print('Input: ', arr)
        print('Result: ', result)
        print('Expected result: ', 2, '\n')


        solution = Solution()
        arr = [1,1,3,3,5,5,7,7]
        result = solution.countElements(arr)
        print('Input: ', arr)
        print('Result: ', result)
        print('Expected result: ', 0, '\n')

        solution = Solution()
        arr = [1,3,2,3,5,0]
        result = solution.countElements(arr)
        print('Input: ', arr)
        print('Result: ', result)
        print('Expected result: ', 3, '\n')

        solution = Solution()
        arr = [1,1,2,2]
        result = solution.countElements(arr)
        print('Input: ', arr)
        print('Result: ', result)
        print('Expected result: ', 2, '\n')


TestSolution().test_CountElements()
