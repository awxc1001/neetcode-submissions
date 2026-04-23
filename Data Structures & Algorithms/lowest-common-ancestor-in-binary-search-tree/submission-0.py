# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #since bst follows   cur.left <= cur <= cur.right, we can use this principle to find first ancestor that seprate p and q on both side
        # or curr_node == p or q
        #if one of two satsify no need to keep checking later because they wont be on different side

        #first we make sure node1 < node2
        node1, node2 = None, None
        if p.val < q.val:
            node1 = p
            node2 = q
        else:
            node1 = q
            node2 = p
        
        return self.find(root, node1, node2)
    
    def find(self, curr, node1, node2):
        #if curr is None, means found nothing till the end
        if curr is None:
            return
        
        #check if satifsy first condition, given two nodes will be in the bst
        if node1.val <= curr.val <= node2.val:
            return curr
        
        #use bst conodtion
        left = None
        right = None
        if curr.val > node2.val:
            left = self.find(curr.left, node1, node2)
        
        elif curr.val < node1.val:
            right = self.find(curr.right, node1, node2)
        
        return left or right
        


        
        