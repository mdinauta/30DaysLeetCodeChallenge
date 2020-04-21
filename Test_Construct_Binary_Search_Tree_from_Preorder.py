from Construct_Binary_Search_Tree_from_Preorder import TreeNode, Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.val), 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 

test_case = [8,5,1,7,10,12]
solution = Solution()
root = solution.bstFromPreorder(test_case)
#inorder(root)
printLevelOrder(root)