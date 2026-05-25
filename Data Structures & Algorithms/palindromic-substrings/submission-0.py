from enum import Enum
import math

# 1. 严格定义状态
class Status(Enum):
    CAN_START = 1   # 自由身：可以选择任意位置作为回文中心
    EXPANDING = 2   # 扩展中：已经确定了中心，正在向两边扩展验证

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        memo = {}

        # 为了完美契合你的函数签名 dp(i, status)，在 EXPANDING 状态下，
        # 我们用一个辅助的指针来记录“右边界”（或者把 i, j 编码进参数）
        # 这里为了严格符合你的 dp(参数, status) 结构，我们让 i 代表左边界，j 代表右边界
        def dp(i: int, j: int, status: Status) -> int:
            # 记忆化搜索缓存
            if (i, j, status) in memo:
                return memo[(i, j, status)]

            # --- 最小问题 Base Case ---
            # 越界了，无法再贡献任何回文串
            if i < 0 or j >= n:
                return 0

            # 初始化你的三个核心变量
            choices = []
            curr_best_ans = 0 # 股票要最大化(-inf)，这里是计数，初始化为0

            # --- 检查当前 status 建立分支 (你的核心逻辑) ---
            if status == Status.CAN_START:
                # 自由身状态下，我们有两个大选择：
                # 1. 启动！以当前 i 为中心（奇数长度回文，如 "aba" 的 'b'）
                choices.append((i, i, Status.EXPANDING, 0)) 
                # 2. 启动！以当前 i 和 i+1 为中心（偶数长度回文，如 "abba" 的 'bb'）
                choices.append((i, i+1, Status.EXPANDING, 0))
                # 3. 不在这里启动，让主函数去遍历其他起点（见下方主循环）

            elif status == Status.EXPANDING:
                # 扩展状态下，我们看当前两端的字符是否相等
                if s[i] == s[j]:
                    # 如果相等！说明我们抓到了一个合法的回文子串！
                    # 钱包变动（回文数变动） +1
                    # 明天的选择：继续向两边撑开 (i-1, j+1)
                    choices.append((i-1, j+1, Status.EXPANDING, 1))
                else:
                    # 如果不相等，这条扩展路就断了，无法继续贡献
                    pass 

            # --- 货比三家 / 收集子答案 (完全套用你的模板) ---
            for future_i, future_j, future_stat, cur_change in choices:
                sub_ans = dp(future_i, future_j, future_stat)
                curr_ans = cur_change + sub_ans
                # 计数问题是累加所有可能性，这里把 max 换成累加
                curr_best_ans += curr_ans

            memo[(i, j, status)] = curr_best_ans
            return curr_best_ans

        # --- 从起点开始动态规划 ---
        total_palindromes = 0
        
        # 每一个位置都有机会作为“中心点”启动状态机
        for k in range(n):
            # 触发奇数长度中心扩展
            total_palindromes += dp(k, k, Status.EXPANDING)
            # 触发偶数长度中心扩展
            total_palindromes += dp(k, k+1, Status.EXPANDING)

        return total_palindromes