from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        # 单调队列：只存索引
        mono_q = deque()
        res = []

        # 开始滑动窗口模板
        while right < len(nums):
            # 1. 扩大窗口
            # 新来一个数，把队列里比它小的都干掉
            while mono_q and nums[mono_q[-1]] <= nums[right]:
                mono_q.pop()
            mono_q.append(right)
            
            # 【严格遵循模板】：让 right 先往前走一步
            right += 1

            # 2. 检查是否需要 shrink 缩小窗口
            # 当当前窗口大小 right - left 大于 k 时，说明左边界该往右缩了
            while right - left > k:
                # 如果要踢掉的左边界 left 正好是队列里的最大值，把它弹出
                if mono_q[0] == left:
                    mono_q.popleft()
                left += 1

            # 3. 经过上面的收缩，此时（当满足长度为 k 时）一定是一个合法的窗口
            if right - left == k:
                res.append(nums[mono_q[0]])

        return res