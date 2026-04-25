# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #本质意思就是：
        #如果当前这棵子树没有任何节点，那就返回空节点。
        if not preorder:
            return None

        root_val = preorder[0]
        #make a root Node
        root = TreeNode(root_val)
        #find root_index
        root_i = inorder.index(root_val)

        #recursively slicing and building and return the built node 
        root.left = self.buildTree(preorder[1 : root_i + 1], inorder[:root_i])
        root.right = self.buildTree(preorder[root_i + 1 :], inorder[root_i + 1 :])
        return root
        