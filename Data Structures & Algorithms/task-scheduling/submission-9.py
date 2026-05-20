class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ① 可用的
        # 当前能做 + 要选最优
        # 👉 max heap
        # ② 冷却的
        # 做完但还不能用（等时间）
        # 👉 queue（带时间）
        # 🔥 一句话本质
        # heap 管“现在做谁最好”
        # queue 管“谁还不能用”

        # 🧩 行为映射（最重要）
        # 每一轮你在干什么：
        # 把“解锁的人”从 queue 放回 heap
        # 从 heap 选最优 task
        # 做完 → 如果还剩 → 放进 queue（标记解锁时间）

        count_map = {}
        cd_time = n

        for task in tasks:
            count_map[task] = count_map.get(task, 0) + 1
        
        #initilaise avaliable pool with max count on the top for process pop
        max_heap = [ (-count, task) for task, count in count_map.items()]
        #python only has min_heap so (-3, "A") ,  (-2, "C"), (-2, "D") in max_heap
        heapq.heapify(max_heap)

        cd_q = deque() #存放task什么时候可以回到heap继续process。 (available_time, -count, task)

        cur_time = 0

        #process all task, should be nothing left in both heap and q
        #   在你previous代码里，你是不管三七二十一，先从 max_heap 弹出一个任务。
        # 这时候如果 max_heap 是空的（比如现在所有任务都在冷却中，CPU 只能被迫待机/Idle），你的代码就会直接报错 IndexError: index out of range。
            #所以，正确的逻辑顺序必须是“以时间为主导”：
        # 时间向前走 1 秒（cur_time += 1）。

        # 看可用的池子（max_heap）：

        # 如果池子里有任务，挑出数量最多的做。
        
        # 再看冷却队列：有没有任务在这一秒“刑满释放”了？如果有，赶紧放回大池子（max_heap）。

        # 如果池子里没有任务，说明这 1 秒只能待机（Idle）。
        while max_heap or cd_q:
            #adavance time
            cur_time += 1

            #check if there is task in ready heap pool
            if max_heap:
                remain, t_name = heapq.heappop(max_heap)
                ## 因为是负数，数量减 1 相当于数学上的加 1
                remain += 1
                # if remain still exist, add to cd_que to process again in future time
                if remain != 0:
                    next_ava_time = cur_time + cd_time
                    info_tuple = (remain, next_ava_time, t_name)
                    cd_q.append(info_tuple)
            
            #check if any in the q can be readded to maxheap pool
            if cd_q:
                #check earliest task ava or not
                ava_time = cd_q[0][1]
                #do pop and heappush if match
                if ava_time == cur_time:
                    remain, ava_time, t_name = cd_q.popleft()
                    heap_tuple = (remain, t_name)
                    #add back in
                    heapq.heappush(max_heap, heap_tuple)
            
            #if both check faield, means its a idle time period, do nothing and wait for ava or cd_q to be ready

        return cur_time





                




