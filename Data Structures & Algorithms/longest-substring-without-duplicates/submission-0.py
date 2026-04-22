class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        
        left = 0
        right = 0
        # 记录结果
        res = 0

        while right < len(s):
            c = s[right]
            # 进行窗口内数据的一系列更新
            window[c] = window.get(c, 0) + 1
            right += 1
            
            # 判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]

                # 进行窗口内数据的一系列更新
                window[d] = window.get(d, 0) - 1
                left += 1
                
            # 在这里更新答案
            res = max(res, right - left)
        return res