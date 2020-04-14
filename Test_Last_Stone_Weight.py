import unittest
from Last_Stone_Weight import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.lastStoneWeight([2,7,4,1,8,1]), 1)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.lastStoneWeight([1]), 1)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.lastStoneWeight([1,1]), 0)

if __name__ == '__main__':
    unittest.main()