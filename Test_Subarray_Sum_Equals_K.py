import unittest
from Subarray_Sum_Equals_K import Solution, BruteForceSolution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = BruteForceSolution()
        nums = [1,1,1] 
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 2)

    def test2(self):
        solution = BruteForceSolution()
        nums = [1,1,1,1]
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 3)

    def test4(self):
        solution = BruteForceSolution()
        nums = [1,1,1,1,1]
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 4)

    def test5(self):
        solution = BruteForceSolution()
        nums = [1,1,1,1,1]
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 4)

    def test6(self):
        solution = BruteForceSolution()
        nums = [1,2,3]
        k = 3
        self.assertEqual(solution.subarraySum(nums, k), 2)

    def test7(self):
        solution = BruteForceSolution()
        nums = [0,0,0,0,0,0,0,0,0,0]
        k = 0
        self.assertEqual(solution.subarraySum(nums, k), 55)

    def test8(self):
        solution = Solution()
        nums = [1,1,1] 
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 2)

    def test9(self):
        solution = Solution()
        nums = [1,1,1,1]
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 3)

    def test10(self):
        solution = Solution()
        nums = [1,1,1,1,1]
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 4)

    def test11(self):
        solution = Solution()
        nums = [1,1,1,1,1]
        k = 2
        self.assertEqual(solution.subarraySum(nums, k), 4)

    def test12(self):
        solution = Solution()
        nums = [1,2,3]
        k = 3
        self.assertEqual(solution.subarraySum(nums, k), 2)

    def test13(self):
        solution = Solution()
        nums = [0,0,0,0,0,0,0,0,0,0]
        k = 0
        self.assertEqual(solution.subarraySum(nums, k), 55)

    def test14(self):
        solution = Solution()
        nums = [1,2,3,4,5]
        k = 0
        self.assertEqual(solution.subarraySum(nums, k), 0)

    def test15(self):
        solution = Solution()
        nums = [3,1,3,6,10]
        k = 7
        self.assertEqual(solution.subarraySum(nums, k), 1)

if __name__ == '__main__':
	unittest.main()
