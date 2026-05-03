import math
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # --- 第一段：建立账本 (Memoization) ---
        # 只要索引 i 相同，从这里爬到顶的最小花费就是固定的
        memo = {}
        
        # 决策选项：走 1 步或 2 步
        step_choices = [1, 2]

        def dp(curr_i):
            # --- 第二段：检查账本 (Lookup) ---
            if curr_i in memo:
                return memo[curr_i]

            # --- 第三段：设定终点与死路 (Base Cases) ---
            # 如果索引达到或超过数组长度，说明已经跨过楼顶，后面不需要再付钱了
            if curr_i >= len(cost):
                return 0
            
            # --- 第四段：多叉树探索与货比三家 (Core Competition) ---
            # 目标是：找出从当前台阶出发，走哪条路后续的花费最少
            smallest_future_cost = math.inf

            for step_val in step_choices:
                # 派出一个递归分身，去问后面几步最少要花多少钱
                res = dp(curr_i + step_val)
                
                # 挑出那个给力（省钱）的子答案
                if res < smallest_future_cost:
                    smallest_future_cost = res

            # --- 第五段：收网总结与加冕 (Post-processing & Reporting) ---
            # 结果 = 支付当前台阶的钱 + 后面台阶最少的钱
            current_total_res = cost[curr_i] + smallest_future_cost
            
            # 存入账本
            memo[curr_i] = current_total_res
            return current_total_res

        # --- 最终调用 ---
        # 题目说可以从 0 或 1 出发，我们比较这两棵决策树的最终账单
        # 计算 dp(0) 时，memo 会被填满；dp(1) 会直接从 memo 拿答案，复杂度 O(N)
        return min(dp(0), dp(1))