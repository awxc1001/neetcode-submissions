from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):

        # 1. 统计频率
        count = Counter(tasks)

        # 2. 最大堆（负数模拟）
        maxHeap = [(-cnt, task) for task, cnt in count.items()]
        heapq.heapify(maxHeap)

        # 3. cooldown 队列
        # (available_time, -cnt, task)
        cooldown = deque()

        time = 0

        while maxHeap or cooldown:

            time += 1

            # 4. 先释放 cooldown 到 heap
            if cooldown and cooldown[0][0] == time:
                _, cnt, task = cooldown.popleft()
                heapq.heappush(maxHeap, (cnt, task))

            # 5. 贪心选择当前最优任务
            if maxHeap:
                cnt, task = heapq.heappop(maxHeap)

                cnt += 1  # 因为是负数

                # 还有剩余 → 放入 cooldown
                if cnt != 0:
                    cooldown.append((time + n + 1, cnt, task))

        return time