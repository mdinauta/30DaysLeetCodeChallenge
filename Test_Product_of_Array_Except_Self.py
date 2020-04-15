import unittest
from Product_of_Array_Except_Self import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])

if __name__ == '__main__':
    unittest.main()