class Solution:
    def __init__(self):
        self.result = []
        self.ans = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #the solution must not contain duplicate subsets
        #sort to group duplicate then pointer skip duplicate
        nums = sorted(nums)
        self.backtrack(nums, 0)
        return self.result
    

    def backtrack(self, nums, start):
        #enter a decsion, append, since we want subset
        self.result.append(self.ans.copy())
        #no need base case since for loop will end when i == len(nums)

        #loop all choices
        for i in range(start, len(nums)):
            #same level
            #only pick branch from left that is first shown, duplicate skip
            if i > start and nums[i] == nums[i - 1]:
                continue

            self.ans.append(nums[i])
            #backtrack
            self.backtrack(nums, i + 1)
            #reset
            self.ans.pop()

        