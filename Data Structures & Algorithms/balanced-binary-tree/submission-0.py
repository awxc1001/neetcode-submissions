# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #“有没有 / 合不合法 / 是否存在”，用全局flag查看
    def __init__(self):
        self.is_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        tree_height = self.dfs_height(root)
        return self.is_balanced
        
    
    def dfs_height(self, cur_node):
        #没孩子了直接返回0，可以先写下面的看看return多少可以满足
        if cur_node is None:
            return 0
        
        #post order traverse start from leaf node back to top
        left_h = self.dfs_height(cur_node.left)
        right_h = self.dfs_height(cur_node.right)

        #every sub differ in height by no more than 1
        if abs(left_h - right_h) > 1:
            self.is_balanced = False
            return -1

        cur_node_h = 1 + max(left_h, right_h)

        return cur_node_h











