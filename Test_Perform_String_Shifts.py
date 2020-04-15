import unittest
from Perform_String_Shifts import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        s = "abc"
        shift = [[0,1],[1,2]]
        self.assertEqual(solution.stringShift(s, shift), "cab")

    def test2(self):
        solution = Solution()
        s = "abcdefg" 
        shift = [[1,1],[1,1],[0,2],[1,3]]
        self.assertEqual(solution.stringShift(s, shift), "efgabcd")


if __name__ == '__main__':
    unittest.main()