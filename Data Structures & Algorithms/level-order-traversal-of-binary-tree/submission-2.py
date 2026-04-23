# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\
        #ensure root, starting node is not None
        if root is None:
            return []

        answer = []
       

        q = deque()
        q.append(root)

        while q:
            #pop out every node of this level
            #the len ensures only nodes of this level are poped
            level_len = len(q)
            level_list = []
            
            for i in range(level_len):
                node = q.popleft()
                #add next level of left and right if there is
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                #add all curr level nodes to level_list
                level_list.append(node.val)
            
            answer.append(level_list)
        
        return answer
                    
                

