class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] * (n+1)

        #fill presum
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        
        #find the largets in the presum array
        #index 0 in presum is place holder
        ans = -math.inf

        # table退化成一个值
        min_prefix = presum[0] # 初始最小前缀和为 0

        for i in range(1, len(presum)):
            #subarray是指两个prefix之间的差

            #先计算 ans，再更新 min_prefix（或者从 i=1 开始循环，确保 min_prefix 始终代表 i 之前的最小值）
            # 核心：用当前前缀和 减去 之前出现过的最小前缀和
            ans = max(ans, presum[i] - min_prefix)
            
            # 更新历史最小前缀和，供下一步循环使用
            min_prefix = min(min_prefix, presum[i])

            
        
        return ans


        