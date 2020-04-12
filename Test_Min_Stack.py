import unittest
from Min_Stack import MinStack

class TestSolution(unittest.TestCase):
    def test1(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)

    def test2(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        stack.pop()
        self.assertEqual(stack.top(), 0)

    def test3(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        stack.pop()
        self.assertEqual(stack.getMin(), -2)

if __name__ == '__main__':
    unittest.main()
