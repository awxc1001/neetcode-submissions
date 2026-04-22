class Solution:
    def __init__(self):
        self.result = []
        self.ans=[]
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #The same number may be chosen from nums an unlimited number of times
        #duplicate if frequency of each of the chosen numbers is the same
        #this means we can have 3334 but not 4333
        #to aovid looking back, we use start as a guard 
        #return list of distintc answer

        #   []
    #     2  5  6  9
    #   2   5  6      
        #but each element pick itself multiple times
        #use i not i + 1 for next level
        self.backtrack_2(nums, target, 0)
        return self.result
    
    def backtrack(self, nums, target, start):
        # 1. 加上“超载”检查，防止死循环
        if sum(self.ans) > target:
            return
        #base case is when found answer 
        if sum(self.ans) == target:
            #append answer and return
            answer = self.ans.copy()
            self.result.append(answer)
            return
            
        #for loop allows us to end loop return
        #loop each choice at same level
        for i in range(start, len(nums)):
            self.ans.append(nums[i])
            self.backtrack(nums, target, i)
            self.ans.pop()
    
    def backtrack_2(self, nums, remain, start):
        # remain 版本
        if remain < 0:
            return
        #base case is when found answer 
        if remain == 0:
            #append answer and return
            answer = self.ans.copy()
            self.result.append(answer)
            return
            
        #for loop allows us to end loop return
        #loop each choice at same level
        for i in range(start, len(nums)):
            remain = remain - nums[i]
            self.ans.append(nums[i])
            self.backtrack_2(nums, remain, i)
            #reset for each level
            remain += self.ans.pop()
            



