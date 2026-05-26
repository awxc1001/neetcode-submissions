class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        total_count = 0

        def expand_from_center(left, right):
            count = 0

            while left >= 0 and right < n and s[left] == s[right]:

                # 当前 left right 是一个回文子串
                count += 1

                #go to next point
                left -= 1
                right += 1

            return count

        for center in range(n):
            # 奇数长度回文，比如 "aba"
            total_count += expand_from_center(center, center)

            # 偶数长度回文，比如 "abba"
            total_count += expand_from_center(center, center + 1)

        return total_count