# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    
    def __init__(self):
        self.max_depth = -math.inf
        self.cur_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.dfs(root)
        return self.max_depth
    
    def dfs(self, root):
        if root is None:
            return
        #enter a node, increase a depth
        self.cur_depth += 1
        #if leaf node
        if root.left is None and root.right is None:
            self.max_depth = max(self.max_depth, self.cur_depth)
        
        self.dfs(root.left)
        self.dfs(root.right)

        #finish both sub backtrack
        self.cur_depth -= 1
