class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # 1. states definition
        start_i = 0

        # state = i
        # dp(i) = 从 s[i] 开始，到结尾，一共有多少种解码方式

        # 2. choices definition
        choices = ["TAKE_ONE_CHAR", "TAKE_TWO_CHARS"]

        memo = {}

        def dp(i):
            state = i

            if state in memo:
                return memo[state]

            # 3. base case

            # 成功走到结尾：
            # 前面做过的一串 choices 已经组成了一种完整解码方式
            if i == n:
                return 1

            # 失败死路：
            # 任何编码都不能从单独的 "0" 开始
            if s[i] == "0":
                return 0

            # 4. initialize answer and choices
            total_current_answer = 0
            future_choices = []

            # 5. generate future choices
            for choice in choices:

                if choice == "TAKE_ONE_CHAR":
                    next_i = i + 1
                    future_choices.append(next_i)

                elif choice == "TAKE_TWO_CHARS":
                    if i + 1 < n:
                        two_digit = int(s[i:i + 2])

                        if 10 <= two_digit <= 26:
                            next_i = i + 2
                            future_choices.append(next_i)

            # 6. try all choices
            for next_i in future_choices:
                total_current_answer += dp(next_i)

            memo[state] = total_current_answer
            return total_current_answer

        return dp(start_i)