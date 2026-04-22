# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_len = 0


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_len(root)
        return self.max_len
    
    def find_len(self, curr):
        if curr is None:
            return 0
        
        curr_len = 1

        curr_left_len = self.find_len(curr.left)
        curr_right_len = self.find_len(curr.right)

        self.max_len = max(self.max_len, curr_left_len + curr_right_len)

        curr_longest = curr_len + max(curr_left_len, curr_right_len)

        return curr_longest
