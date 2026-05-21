from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        # 单调队列：只存索引,这就是我们的window
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

        # mono_q = deque()  # 单调队列，里面存 (index, val) 元组，val 从大到小排列
        # fast = 0          # 右指针，代表当前正要吃进窗口的元素位置
        # slow = 0          # 左指针，代表当前窗口的逻辑左边界
        # len_n = len(nums)

        # window = []       # 真实的窗口数组，存 (index, val) 元组
        # answer = []       # 存放最终结果的数组

        # while fast < len_n:
        #     # ---------------------------------------------------------------
        #     # 1. 扩大窗口：无脑把当前 fast 指向的新元素吃进 window 和 mono_q
        #     # ---------------------------------------------------------------
        #     tuple_info = (fast, nums[fast])
        #     window.append(tuple_info)

        #     # 弹出队列尾部所有比新来元素小的数（它们已经不可能成为未来窗口的最大值了）
        #     while mono_q and mono_q[-1][1] <= nums[fast]:
        #         mono_q.pop()
            
        #     # 把新元素安全压入队列
        #     mono_q.append(tuple_info)

        #     # 【核心模板节奏】：让右指针往前迈一步。
        #     # 此时 fast 变成了下一个位置，当前窗口在指针上的虚拟长度就是 (fast - slow)
        #     fast += 1

        #     # ---------------------------------------------------------------
        #     # 2. 检查并擦屁股：如果窗口超长了（长度达到 k + 1），立刻触发裁剪
        #     # ---------------------------------------------------------------
        #     # 核心卡点：
        #     # - 当第一次凑齐 k 个数时：fast - slow 刚好等于 k，这个 while 条件不成立！
        #     # - 也就是说，第一次凑齐答案时，这里直接被跳过，根本不会执行裁剪大刀！
        #     while fast - slow > k:
        #         # 【🚨 最关键的逻辑卡点】：这里必须写 == slow 绝对不能写 < slow ！
        #         #
        #         # 为什么？因为此时代码是一行行执行的，下面的 slow += 1 还没有发生！
        #         # 这一瞬间，slow 对应的正是当下【马上就要被无情扔掉】的那个老左边界索引。
        #         # 
        #         # 如果单调队列的队头（最大值位置）刚好就是这个准备被淘汰的 slow：
        #         # 1. 写 == slow 或 <= slow：(slow == slow) 成立，过期的大数被完美拦截并 popleft() 弹出。
        #         # 2. 写 < slow：(slow < slow) 变成不成立！代码会直接跳过弹出，导致过期的死鬼最大值留在队列里，污染后面的答案！
        #         # 事实上，因为每次循环窗口最多只超长 1 个数，面临淘汰的永远只有当前这一个 slow。
        #         # 比 slow 还要小的旧索引，在以前的轮次里早死光了。所以写 == slow 才是最纯粹、最精准的拦截。
        #         if mono_q[0][0] == slow:
        #             mono_q.popleft()
                
        #         # 真实数组和左指针同步向右移动一格，完成裁剪
        #         window.pop(0)
        #         slow += 1

        #     # ---------------------------------------------------------------
        #     # 3. 收集答案：经过上面的裁剪（或滑过），此时窗口必然处于百分之百合法状态
        #     # ---------------------------------------------------------------
        #     # - 第一次凑齐 k 个数那一轮：上面第 2 步被跳过，来到这里 len(window) 正好是 k，顺利拿下第一个答案！
        #     # - 之后的每一轮：由于第 2 步会把超长的 (k+1) 裁剪回 k，来到这里时长度也必定是 k，连续拿下后续答案！
        #     if len(window) == k:
        #         answer.append(mono_q[0][1])  # 队头永远是当前合法窗口里的最大值
        
        # return answer





        