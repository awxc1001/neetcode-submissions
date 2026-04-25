# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_sum = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.calculate(root)
        return self.max_sum
    
    def calculate(self, root):
        if root is None:
            return 0
        
        left_p_sum = self.calculate(root.left)
        right_p_sum = self.calculate(root.right)
        #postorder to leaf node and bot up to subtree root
        #a path must have a subtree root node to connect edge btw left
        #and right
        #to achive maxium, we make negative p_sum to 0
        left_p_sum = max(0, left_p_sum)
        right_p_sum = max(0, right_p_sum)
        
        #calculate current valid path and update
        curr_path_sum = root.val + left_p_sum + right_p_sum
        self.max_sum = max(self.max_sum, curr_path_sum)

        #after calcuting max pathsum of this node, we can only
        #return one side as a path to its parent
        #so a bigger side will be returned
        #lucky our every node operation has removed neagtive answers
        return max(root.val + left_p_sum, root.val + right_p_sum)
        