# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.number_of_nodes = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.number_of_nodes = max(self.number_of_nodes, L+R+1)
            return max(L, R) + 1

        depth(root)
        # subtract 1 to go from nodes to edges
        return self.number_of_nodes - 1