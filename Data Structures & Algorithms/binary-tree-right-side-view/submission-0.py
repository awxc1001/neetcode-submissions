# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #exclude if root is None
        if root is None:
            return []
        
        result = []
        q = deque()
        q.append(root)

        while q:
            level_len = len(q)

            for i in range(level_len):
                curr_node = q.popleft()
                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
                #now we store the rightest, i = level_len-1 in to result
                if i == level_len - 1:
                    result.append(curr_node.val)
        
        return result


        