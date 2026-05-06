class Solution:
    def rob(self, nums: List[int]) -> int:
        #0 for current house index, 1 for next house index
        choices = [0, 1]
        n = len(nums)
        #if choose 0, then its curr_i val + dp(cur_i +2) val
        #if choose 1, then its dp(curr_i + 1) val

        #special case
        if n == 1:
            return nums[0]

        def dp(start_i, end_i, choices, memo):
            # 闭区间 [start_i, end_i]
            # 超过右边界才停
            if start_i > end_i:
                return 0

            if start_i in memo:
                return memo[start_i]

            for choice in choices:
                if choice == 0:
                    # 抢当前房子
                    sub_ans1 = nums[start_i] + dp(start_i + 2, end_i, choices, memo)
                elif choice == 1:
                    # 不抢当前房子
                    sub_ans2 = dp(start_i + 1, end_i, choices, memo)

            curr_best_ans = max(sub_ans1, sub_ans2)
            memo[start_i] = curr_best_ans
            return curr_best_ans

        #since head and tail are neigbors, we cant decide from a future point
        #we use two dp tree to get both answers
        #这里的n-1 n-2是闭区间，要包含的
        #所以basecase 是超过他们
        #如果是n和n-1，那就是不包含的开区间，大于等于

        memo1 = {}
        dp1 = dp(1, n - 1, choices, memo1)

        memo2 = {}
        dp2 = dp(0, n - 2, choices, memo2)

        return max(dp1, dp2)
        