# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # top down sub problem apporach
        # root no need to change, left and right keep swaping
        if root is None:
            return
        
        #Invert the binary tree and return its root.
        self.invert(root)
        return root

    def invert(self, cur_node):
        if cur_node is None:
            return
            
        # 1. 我先把我的活干了：左右互换位置
        cur_node.left, cur_node.right = cur_node.right, cur_node.left
        
        # 2. 我换完了，剩下的细节你们自己去搞定
        self.invert(cur_node.left)
        self.invert(cur_node.right)

        

        

        