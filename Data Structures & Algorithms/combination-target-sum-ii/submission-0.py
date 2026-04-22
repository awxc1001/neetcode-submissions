class Solution:
    def __init__(self):
        self.result = []
        self.ans = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Each element from candidates may be chosen at most once within a combination. 
        #The solution set must not contain duplicate combinations.
        #use start to block looking backwards and use i + 1 to not pick same
        #but since candidate has duplicate, means each level we need to skip
        #to avoid duplicate answers, for example
        #[9,2,2,4,6,1,5], target = 8,可以有2个[2,1,5]
        #same level，横向去除就要sorted然后i>start i-1 == i操作
        candidates = sorted(candidates)
        self.backtrack(candidates, target, 0)
        return self.result
    
    def backtrack(self, candidates, remain, start):
        #base case
        if remain < 0:
            return
        
        if remain == 0:
            self.result.append(self.ans.copy())
            return


        for i in range(start, len(candidates)):
            #same level,横向去重复，直接把一样初始选项砍了
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            remain -= candidates[i]
            self.ans.append(candidates[i])

            #next level, no looking back or choose same
            self.backtrack(candidates, remain, i + 1)
            #reset after a level finish
            remain += self.ans.pop()