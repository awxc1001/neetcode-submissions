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
        # 递归会后序走到叶子节点
        # 如果整棵树只有一个节点，那么 diameter 仍然是 0，因为没有任何 edge

        # 当前节点作为拐点，更新经过它的最长路径
        self.max_len = max(self.max_len, left + right)

        # 返回给父节点的只能是单边长度
        # 因为父节点如果继续往上接，路径必须保持一条线，不能把左右两边一起带上去
        # 这个return步不会影响max—len答案，如果就只有一个root节点的话
        return 1 + max(left, right)