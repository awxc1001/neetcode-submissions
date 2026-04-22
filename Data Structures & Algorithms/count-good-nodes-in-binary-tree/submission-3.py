# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.good_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        #1 <= number of nodes in the tree <= 100
        #-100 <= Node.val <= 100
        #contains no nodes with a value greater than the value of node x
        #root上面没啥节点，传一个不存在的low number  -math.inf, -100000
        self.traverse(root, -math.inf)
        return self.good_count
    
    def traverse(self, cur, x_val):
        if cur is None:
            return 
        
        #人话翻译只要不小于全局路径最大值，就是 good node
        if cur.val >= x_val:
            self.good_count += 1
            #每次统计
            x_val = cur.val

        # elif cur.val < x_val:啥也不用做


        #check left and right sub
        self.traverse(cur.left, x_val)
        self.traverse(cur.right, x_val)
        #post order do nothing

        
        






        