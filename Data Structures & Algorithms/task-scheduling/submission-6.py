from typing import List
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # 1. 统计频率
        count_map = {}
        for t in tasks:
            count_map[t] = count_map.get(t, 0) + 1

        # 2. max heap（用负数模拟）
        max_heap = [(-cnt, task) for task, cnt in count_map.items()]
        heapq.heapify(max_heap)

        # 3. cooldown queue: (ready_time, -count, task)
        cd_q = deque()

        cur_time = 0

        while max_heap or cd_q:

            cur_time += 1

            # 1) 先把“已经到时间”的任务放回 heap
            while cd_q and cd_q[0][0] <= cur_time:
                ready_time, neg_cnt, task = cd_q.popleft()
                heapq.heappush(max_heap, (neg_cnt, task))

            # 2) 从 heap 选任务执行
            if max_heap:
                neg_cnt, task = heapq.heappop(max_heap)
                neg_cnt += 1  # 因为是负数

                # 3) 如果还没做完，放入 cooldown
                if neg_cnt != 0:
                    cd_q.append((cur_time + n + 1, neg_cnt, task))

            # else: idle（什么都不做）

        return cur_time