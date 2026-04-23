# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.target = -10000
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #bst in order traverse is smallest to largest order
        self.find(root, k)
        return self.target
    
    def find(self, root, k):
        if root is None:
            return
        
        self.find(root.left, k)
        self.count += 1
        if self.count == k:
            self.target = root.val
            return
        self.find(root.right, k)

