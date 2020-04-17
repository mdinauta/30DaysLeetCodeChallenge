import unittest
from Number_of_Islands import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        test_case = [["1","1","1","1","0"],
                     ["1","1","0","1","0"],
                     ["1","1","0","0","0"],
                     ["0","0","0","0","0"]]
        self.assertEqual(solution.numIslands(test_case), 1)

    def test2(self):
        solution = Solution()
        test_case = [["1","1","0","0","0"],
                     ["1","1","0","0","0"],
                     ["0","0","1","0","0"],
                     ["0","0","0","1","1"]]
        self.assertEqual(solution.numIslands(test_case), 3)

    def test3(self):
        solution = Solution()
        test_case = [["1","0","1","1","0","1","1"]]
        self.assertEqual(solution.numIslands(test_case), 3)

if __name__ == '__main__':
    unittest.main()