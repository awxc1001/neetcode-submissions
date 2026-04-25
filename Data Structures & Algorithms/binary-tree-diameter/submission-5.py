class Solution:
    def __init__(self):
        self.max_len = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_len(root)
        return self.max_len
    
    def find_len(self, curr):
        if curr is None:
            return 0
        
        left = self.find_len(curr.left)
        right = self.find_len(curr.right)
        #后续到叶子节点，如果就root一个节点，那其实没有edge边
        #len就是0

        # 当前节点作为拐点，更新经过它的最长路径
        self.max_len = max(self.max_len, left + right)

        # 返回给父节点的最长单边长度，因为path必须节点能连一条线
        # 不会影响max——len答案，如果就只有一个节点的话
        return 1 + max(left, right)