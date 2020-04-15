import unittest
from Contiguous_Array import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0,1]), 2)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0,1,0]), 2)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0,1,0,1]), 4)

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0,0,1,1,1,1]), 4)

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0,0,1,1,1,1,1,1,0,1]), 4)

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0,0,1,0,0,0,1,1]), 6)

if __name__ == '__main__':
    unittest.main()