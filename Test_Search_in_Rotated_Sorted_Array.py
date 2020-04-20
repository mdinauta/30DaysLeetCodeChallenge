import unittest
from Search_in_Rotated_Sorted_Array import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(solution.search(nums, 0), 4)

    def test2(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(solution.search(nums, 3), -1)

    def test3(self):
        solution = Solution()
        nums = []
        self.assertEqual(solution.search(nums, 5), -1)

    def test4(self):
        solution = Solution()
        nums = [1]
        self.assertEqual(solution.search(nums, 1), 0)

    def test5(self):
        solution = Solution()
        nums = [1,2]
        self.assertEqual(solution.search(nums, 1), 0)

    def test6(self):
        solution = Solution()
        nums = [1,2]
        self.assertEqual(solution.search(nums, 2), 1)

    def test7(self):
        solution = Solution()
        nums = [1,2,3]
        self.assertEqual(solution.search(nums, 2), 1)

    def test8(self):
        solution = Solution()
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(solution.search(nums, 2), 6)

    def test9(self):
        solution = Solution()
        nums = [3,1]
        self.assertEqual(solution.search(nums, 1), 1)

    def test10(self):
        solution = Solution()
        nums = [7,8,1,2,3,4,5,6]
        self.assertEqual(solution.search(nums, 2), 3)

    def test11(self):
        solution = Solution()
        nums = [7,8,1,2,3,4,5,6]
        self.assertEqual(solution.search(nums, 6), 7)

if __name__ == '__main__':
    unittest.main()