import math
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # 状态定义：CAN_BUY=可买 / HOLDING=持有 / SELL_FINISH=结束
        CAN_BUY = "CAN_BUY"
        HOLDING = "HOLDING"
        SELL_FINISH = "SELL_FINISH"

        # 初始状态：一开始没有股票，所以可以买
        initial_status = CAN_BUY

        memo = {}

        def dp(i, status):
            # 记忆化
            if (i, status) in memo:
                return memo[(i, status)]

            # 终止：到最后一天 or 已结束交易
            if i == n or status == SELL_FINISH:
                return 0

            curr_best = -math.inf
            future_choices = []

            # 状态转移
            if status == CAN_BUY:
                # 买 / 不买
                future_choices.append((i + 1, HOLDING, -prices[i]))
                future_choices.append((i + 1, CAN_BUY, 0))

            elif status == HOLDING:
                # 卖 / 不卖
                future_choices.append((i + 1, SELL_FINISH, prices[i]))
                future_choices.append((i + 1, HOLDING, 0))

            # 枚举所有选择取最大
            for ni, ns, gain in future_choices:
                curr_best = max(curr_best, gain + dp(ni, ns))

            memo[(i, status)] = curr_best
            return curr_best

        return dp(0, initial_status)