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

        # 2. 中序位置操作
        # can加一个优化：如果已经找到了 target，就没必要继续计数了
        # if self.target != -10000: 
        #     return
        self.count += 1
        if self.count == k:
            self.target = root.val
            return
            
        self.find(root.right, k)

