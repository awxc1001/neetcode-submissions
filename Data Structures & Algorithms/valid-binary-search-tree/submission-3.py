class Solution:
    def __init__(self):
        self.is_bst = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.bst_check(root, float('-inf'), float('inf'))
        return self.is_bst
    
    def bst_check(self, root, low, high):
        if root is None:
            return
        
        if not (low < root.val < high):
            self.is_bst = False
            return
        
        # check left
        self.bst_check(root.left, low, root.val)
        
        # check right
        self.bst_check(root.right, root.val, high)