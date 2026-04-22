class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        # self.used = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        #start from 0
       #    [] 
    #     / | \ 
    #   1   2  3
    # 12 13 23
    # 123   
        self.backtrack(nums, 0)
        return self.result

    def backtrack(self, nums, start):
        #subset include empty, single number, no need base case
        #since the for loop will end 
        self.result.append(self.path.copy())
        
        #check neibo and choices at each start point
        for i in range(start, len(nums)):
            #不需要used
            #如果 12 和 21 算 同一个 就用 start（不让回头选，只能往后挑），
            #如果算 不同的 就用 used（允许回头选）。
            #pick a choice and mark as used
            self.path.append(nums[i])
            #go to next level choices
            
        # for i in range(start, len(nums)) 循环里：
        # start是这一关的负责人，只能从这里开始往后挑。”
        # 现在挑中了第 i 个。为了让下一关的人别再挑选过的、或者跳过的，
        # 我要告诉他们从 i + 1 开始挑
            self.backtrack(nums, i + 1)
            
            #reach base case go back, reset to original status at each level
            self.path.pop()

                