# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, cur_node, num):
        if num < cur_node.val:
            if cur_node.left:
                cur_node = cur_node.left
                self.insert(cur_node, num)
            else:
                cur_node.left = TreeNode(num)
        else:
            if cur_node.right:
                cur_node = cur_node.right
                self.insert(cur_node, num)
            else:
                cur_node.right = TreeNode(num)
        return

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        for num in preorder[1:]:
            cur_node = root
            self.insert(cur_node, num)
        return root
