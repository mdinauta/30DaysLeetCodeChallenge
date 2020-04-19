import unittest
from Minimum_Path_Sum import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        test_case = [
                      [1,3,1],
                      [1,5,1],
                      [4,2,1]
                    ]
        self.assertEqual(solution.minPathSum(test_case), 7)

    def test2(self):
        solution = Solution()
        test_case = [[1,2],[1,1]]
        self.assertEqual(solution.minPathSum(test_case), 3)

if __name__ == '__main__':
    unittest.main()