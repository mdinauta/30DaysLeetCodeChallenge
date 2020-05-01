from Bitwise_AND_of_Numbers_Range import Solution
import unittest

class Test(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.rangeBitwiseAnd(5,7), 4) 

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.rangeBitwiseAnd(0,1), 0)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.rangeBitwiseAnd(0,2), 0)


if __name__ == '__main__':
    unittest.main()