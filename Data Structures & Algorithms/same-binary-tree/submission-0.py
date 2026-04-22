# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
    
    def dfs(self, p, q):
        #base case
        if p is None:
            return p == q
        if q is None:
            return q == p
        
        #要一路往下看，所以别这么写
        # if p.val == q.val:
        #     return True

        if p.val != q.val:
            return False
        
        #check subs
        is_left_same = self.dfs(p.left, q.left)
        is_right_same = self.dfs(p.right, q.right)

        return (is_left_same and is_right_same)