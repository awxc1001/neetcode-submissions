import math
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # states definition
        CAN_BUY = "CAN_BUY"
        HOLDING = "HOLDING"
        SELL_FINISH = "SELL_FINISH"

        initial_state = (0, CAN_BUY)

        # choices definition
        choices_by_status = {
            CAN_BUY: ["BUY", "SKIP_BUY"],
            HOLDING: ["SELL", "SKIP_SELL"],
            SELL_FINISH: []
        }

        memo = {}

        def dp(i, status):
            state = (i, status)

            if state in memo:
                return memo[state]

            if i == n or status == SELL_FINISH:
                return 0

            best_current_answer = -math.inf
            future_choices = []

            # generate future choices
            for choice in choices_by_status[status]:

                if choice == "BUY":
                    next_i = i + 1
                    next_status = HOLDING
                    gain = -prices[i]

                elif choice == "SKIP_BUY":
                    next_i = i + 1
                    next_status = CAN_BUY
                    gain = 0

                elif choice == "SELL":
                    next_i = i + 1
                    next_status = SELL_FINISH
                    gain = prices[i]

                elif choice == "SKIP_SELL":
                    next_i = i + 1
                    next_status = HOLDING
                    gain = 0

                future_choices.append((next_i, next_status, gain))

            # choose best answer
            for next_i, next_status, gain in future_choices:
                best_current_answer = max(
                    best_current_answer,
                    gain + dp(next_i, next_status)
                )

            memo[state] = best_current_answer
            return best_current_answer

        return dp(*initial_state)