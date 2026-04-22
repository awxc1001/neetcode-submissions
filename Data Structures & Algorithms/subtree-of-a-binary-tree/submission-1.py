# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def __init__(self):
        is_sub_tree = False
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #1 <= The number of nodes in both trees <= 100
        #we try find the subTree start point on the big tree
        #if we cant find till the end then means we cant
        if root is None:
            return False
        

        # 2. 尝试以当前 root 为起点，看它和 subRoot 是不是同一棵树
        if root.val == subRoot.val:
            if self.is_same_tree(root, subRoot):
                return True # 找到了，直接逐层上报 True
        
        # 3. 核心：如果当前点不是起点，就去左边找，或者去右边找
        # 只要有一边能找到，就返回 True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, root1, root2):
        #current node pair check
        #if reach end or None on both side
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        left = self.is_same_tree(root1.left, root2.left)
        right = self.is_same_tree(root1.right, root2.right)

        return (left and right)