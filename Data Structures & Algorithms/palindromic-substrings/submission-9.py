import sys
# 👈 核心：将 Python 的最大递归深度放大，防止超长字符串爆栈
sys.setrecursionlimit(30000)

# STATUS constant
CAN_START = "START"
MATCHING = "MATCH"

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dp(left: int, right: int, status: str) -> int:
            # 1. smallest subproblem as basecase, off boundary no more
            if left < 0 or right >= n:
                return 0

            if (left, right, status) in memo:
                return memo[(left, right, status)]

            # generate valid future decisions based on status
            future_choices = []
            curr_best_ans = 0

            # 2. 根据当前状态，构建决策分支
            if status == CAN_START:
                i = left 
                if i < n:
                    # 分支 A：奇数长度回文串起点
                    odd_tuple = (i, i, MATCHING, 0)
                    # 分支 B：偶数长度回文串起点
                    even_tuple = (i, i + 1, MATCHING, 0)
                    # 分支 C：继续寻找下一个起点
                    next_start_tuple = (i + 1, i + 1, CAN_START, 0)
                    
                    future_choices.append(odd_tuple)
                    future_choices.append(even_tuple)
                    future_choices.append(next_start_tuple)

            elif status == MATCHING:
                # 如果两端字符相等，这是一个有效的回文串！
                if s[left] == s[right]:
                    # 收益 +1，继续向外层扩展匹配
                    expand_tuple = (left - 1, right + 1, MATCHING, 1)
                    future_choices.append(expand_tuple)

            # loop check future choices to generate answer for curr_best
            for future_left, future_right, future_stat, cur_change in future_choices:
                sub_ans = dp(future_left, future_right, future_stat)
                curr_ans = cur_change + sub_ans
                
                # 在 CAN_START 状态下，累加所有平行独立分支的结果
                if status == CAN_START:
                    curr_best_ans += curr_ans
                else:
                    curr_best_ans = curr_ans

            memo[(left, right, status)] = curr_best_ans
            return curr_best_ans

        # we begin from start_i
        start_left = 0
        start_right = 0
        start_status = CAN_START
        ans = dp(start_left, start_right, start_status)

        return ans