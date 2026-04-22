class Solution:
    def __init__(self):
        self.result = []
        self.ans = []
        self.used = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.used = [False] * n
        #这里start其实没用，因为都是从头开始，但是写可以增强理解
        self.backtrack(nums, 0)
        return self.result
    

    def backtrack(self, nums, start):
        #base case
        if len(self.ans) == len(nums):
            #possible permutation found
            self.result.append(self.ans.copy())
            return
        
        for i in range(0, len(nums)):
            #skip already used
            if self.used[i] is False:
                #same level append
                self.ans.append(nums[i])
                self.used[i] = True

                #只有状态合法才可以递归
                #结论 1：只有没用过才递归
                #因为递归表示“基于当前新选择继续往下探索”，
                #如果这个数已经用过，就没有形成新的合法状态，不能递归
                self.backtrack(nums, 0)

                #只有backtrack，才能修复状态，不要写外面
                #结论 2：used[i] = False 不会错
                #因为它撤销的正是这一轮循环刚刚做的选择，
                #和 append(nums[i])、used[i] = True 是严格配对的。
                self.ans.pop()
                self.used[i] = False
            
        