class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            elif nums[i] != 1:
                #reset
                max_count = max(max_count, current)
                current = 0

        #if never meet a zero at the end after any reset, or never need to reset    
        return max(max_count, current)
        