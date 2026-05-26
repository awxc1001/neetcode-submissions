from typing import List


class Solution:

    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # 1. states definition
        # state = (left, right)
        # dp(left, right) = s[left:right + 1] 是否是回文

        # 2. choices definition
        choices = ["CHECK_BOTH_ENDS"]

        memo = {}

        def dp(left, right):
            state = (left, right)

            if state in memo:
                return memo[state]

            # 3. base case
            if left >= right:
                return True

            # 4. initialize answer and choices
            current_answer = False
            future_choices = []

            # 5. generate future choices
            for choice in choices:

                if choice == "CHECK_BOTH_ENDS":
                    if s[left] == s[right]:
                        next_left = left + 1
                        next_right = right - 1

                        future_choices.append((next_left, next_right))

            # 6. try all choices
            for next_left, next_right in future_choices:
                if dp(next_left, next_right):
                    current_answer = True

            memo[state] = current_answer
            return current_answer

        total_count = 0

        # 枚举所有 substring 的区间
        for left in range(n):
            for right in range(left, n):
                if dp(left, right):
                    total_count += 1

        return total_count