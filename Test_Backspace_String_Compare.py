import unittest
from Backspace_String_Compare import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        S = 'ab#c'
        T = 'ad#c'
        self.assertEqual(solution.backspaceCompare(S, T), True)

    def test2(self):
        solution = Solution()
        S = 'ab##'
        T = 'c#d#'
        self.assertEqual(solution.backspaceCompare(S, T), True)

    def test3(self):
        solution = Solution()
        S = 'a##c'
        T = '#a#c'
        self.assertEqual(solution.backspaceCompare(S, T), True)

    def test4(self):
        solution = Solution()
        S = 'a#c'
        T = 'b'
        self.assertEqual(solution.backspaceCompare(S, T), False)

    def test5(self):
        solution = Solution()
        S = 'y#fo##f'
        T = 'y#f#o##f'
        self.assertEqual(solution.backspaceCompare(S, T), True)

if __name__ == '__main__':
    unittest.main()