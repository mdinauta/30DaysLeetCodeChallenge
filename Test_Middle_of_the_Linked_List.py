import unittest
from Middle_of_the_Linked_List import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TestSolution(unittest.TestCase):
    def test1(self):
        n5 = ListNode(5)
        n4 = ListNode(4)
        n4.next = n5
        n3 = ListNode(3)
        n3.next = n4
        n2 = ListNode(2)
        n2.next = n3
        n1 = ListNode(1)
        n1.next = n2
        solution = Solution()
        self.assertEqual(solution.middleNode(n1).val, n3.val)

    def test2(self):
        n1 = ListNode(1)
        solution = Solution()
        self.assertEqual(solution.middleNode(n1).val, n1.val)

    def test3(self):
        n6 = ListNode(6)
        n5 = ListNode(5)
        n5.next = n6
        n4 = ListNode(4)
        n4.next = n5
        n3 = ListNode(3)
        n3.next = n4
        n2 = ListNode(2)
        n2.next = n3
        n1 = ListNode(1)
        n1.next = n2
        solution = Solution()
        self.assertEqual(solution.middleNode(n1).val, n4.val)



if __name__ == '__main__':
    unittest.main()
