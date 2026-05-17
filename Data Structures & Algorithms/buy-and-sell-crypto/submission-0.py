class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0

        memo = {}

        def dp(i, status):
            # 1. 查账本
            if (i, status) in memo:
                return memo[(i, status)]

            # 2. 撞终点
            if i == n or status == 'FINISH':
                return 0

            # 3. 画树枝
            best_sub_answer = -math.inf
            choices = []

            if status == 'CAN_BUY':
                choices.append((i + 1, 'CAN_BUY', 0))          # 不买
                choices.append((i + 1, 'HOLD', -prices[i]))     # 买入

            elif status == 'HOLD':
                choices.append((i + 1, 'HOLD', 0))             # 不卖
                choices.append((i + 1, 'FINISH', prices[i]))    # 卖出

            # 4. 货比三家
            for next_i, next_status, money_change in choices:
                sub_answer = dp(next_i, next_status)
                total = sub_answer + money_change
                best_sub_answer = max(best_sub_answer, total)

            # 5. 写账本
            memo[(i, status)] = best_sub_answer
            return best_sub_answer

        # 入口：第 0 天，清白之身
        return dp(0, 'CAN_BUY')