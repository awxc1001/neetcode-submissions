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
        
        left_sub = self.invert(cur_node.left)
        right_sub = self.invert(cur_node.right)

        #下面翻转好了，
        cur_node.left = right_sub
        cur_node.right = left_sub

        # 错误点：这里必须返回 cur_node，否则上一层拿到的 left_sub 和 right_sub 都是 None
        return cur_node 


        

        

        