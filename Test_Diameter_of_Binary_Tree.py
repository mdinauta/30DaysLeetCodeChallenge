import unittest
from Diameter_of_Binary_Tree import TreeNode, Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        node5 = TreeNode(5)
        node4 = TreeNode(4)
        node3 = TreeNode(3)

        node2 = TreeNode(2)
        node2.left = node4
        node2.right = node5

        node1 = TreeNode(1)
        node1.left = node2
        node1.right = node3

        self.assertEqual(Solution().diameterOfBinaryTree(node1), 3)

    def test2(self):

        node6 = TreeNode(6)
        node5 = TreeNode(5)
        node4 = TreeNode(4)

        node3 = TreeNode(3)
        node3.left = node4
        node3.right = node5

        node2 = TreeNode(2)
        node2.left = node3
        node2.right = node6

        node1 = TreeNode(1)
        node1.left = node2

        self.assertEqual(Solution().diameterOfBinaryTree(node1), 3)



if __name__ == '__main__':
    unittest.main()
