class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. 定义：将所有数取反，建立最小堆（逻辑上的最大堆）
        #1 <= stones.length <= 20
        #1 <= stones[i] <= 100
        max_heap = [-st for st in stones]
        heapq.heapify(max_heap)
        if len(stones) == 1:
            return stones[0]
 

        #At each step we choose the two heaviest stones, with weight x and y and smash them together

        #do one normal run
        #get the two heaviest
        
        #now make it as loop, stop when only one stone left，这个理解成只要还有至少两块石头就继续撞最好
        while len(max_heap) > 1:
            biggest_1 = heapq.heappop(max_heap)
            biggest_2 = heapq.heappop(max_heap)

            #if x == y, both stones are destroyed
            if biggest_1 == biggest_2:
                continue
            # #If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
            # elif x < y:
            #     new_stone = y - x
            #     heapq.heappush(max_heap, new_stone)
            
            # else:
            #     new_stone = x - y
            #     heapq.heappush(max_heap, new_stone)

            #Remeber the first one pop from heap is always the biggest, second pop either equal or small, just remeber this
            else:
                new_stone = biggest_1 - biggest_2
                heapq.heappush(max_heap, new_stone)
        
        #最后要么剩一块，要么全碎了，记得-改回来
        #if list 这个空和NOne都会false
        return - max_heap[0] if max_heap else 0

        