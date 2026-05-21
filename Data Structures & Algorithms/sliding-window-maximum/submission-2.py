from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque()

        fast = 0
        slow = 0

        len_n = len(nums)
        window = []
        answer = []

        while fast < len_n:
            tuple_info = (fast, nums[fast])
            window.append(tuple_info)
            
            while mono_q and mono_q[-1][1] <= nums[fast]:
                mono_q.pop()

            mono_q.append(tuple_info)
            
            # 【修正 2】: 收集答案必须拿数值 [1]，而不是索引 [0]
            if len(window) == k:
                answer.append(mono_q[0][1])
            
            fast += 1
            
            # shrink window condition
            while slow < fast and len(window) == k:
                # 【修正 3】: 因为接下来 slow 马上要 +1 了，所以当前等于 slow 的下标就是被淘汰的
                max_i, max_val = mono_q[0]
                if max_i == slow:
                    mono_q.popleft()
                
                # 【修正 1】: 必须用 pop(0) 弹出最左边的老元素，否则会陷入死循环！
                window.pop(0)
                slow += 1
        
        return answer