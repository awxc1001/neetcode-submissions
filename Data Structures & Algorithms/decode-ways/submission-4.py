class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        # state:
        # dp(i) = number of ways to decode s[i:]

        start_i = 0

        # choice table
        choice_future_state = {

            "decode_one": {

                # legality
                "valid": lambda i:
                    i < n and s[i] != "0",

                # future state
                "future_state": lambda i:
                    i + 1
            },

            "decode_two": {

                "valid": lambda i:
                    (
                        i + 1 < n and
                        10 <= int(s[i:i+2]) <= 26
                    ),

                "future_state": lambda i:
                    i + 2
            }
        }

        memo = {}

        def dp(i):

            # successfully decoded everything
            if i == n:
                return 1

            # invalid overflow
            if i > n:
                return 0

            if i in memo:
                return memo[i]

            total = 0

            # try every choice
            for choice_name in choice_future_state:

                choice_info = choice_future_state[choice_name]

                # check legality
                if choice_info["valid"](i):

                    # transition to future state
                    future_i = choice_info["future_state"](i)

                    total += dp(future_i)

            memo[i] = total
            return total

        return dp(start_i)