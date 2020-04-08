import unittest
from Counting_Elements import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        arr = [1,2,3]
        self.assertEqual(solution.countElements(arr), 2)

    def test2(self):
        solution = Solution()
        arr = [1,1,3,3,5,5,7,7]
        self.assertEqual(solution.countElements(arr), 0)

    def test3(self):
        solution = Solution()
        arr = [1,3,2,3,5,0]
        self.assertEqual(solution.countElements(arr), 3)

    def test4(self):
        solution = Solution()
        arr = [1,1,2,2]
        self.assertEqual(solution.countElements(arr), 2)

if __name__ == '__main__':
    unittest.main()
