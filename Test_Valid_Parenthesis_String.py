import unittest
from Valid_Parenthesis_String import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('()'), True)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('(*)'), True)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('(*))'), True)

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('('), False)

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString(''), True)

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('**))'), True)

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('**)'), True)

    def test7(self):
        solution = Solution()
        self.assertEqual(solution.checkValidString('(())((())()()(*)(*()(())())())()()((()())((()))(*'), False)

if __name__ == '__main__':
    unittest.main()