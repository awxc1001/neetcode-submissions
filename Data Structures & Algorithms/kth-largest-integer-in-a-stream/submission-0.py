class KthLargest:

    def __init__(self, k: int, nums: List[int]):
            # 1. 直接引用 nums（或者用 nums.copy() 保护原数据）
            self.mini_heap = nums
            self.k_counts = k
            
            # 2. 原地堆化，此时 self.mini_heap[0] 是最小的
            #heapify 真的没有 return。它和 Python 列表的 sort() 方法在行为上是一模一样的：它们都属于 “原地修改”（In-place operation）。
            #. 对比一下这两个“没有返回值”的家伙方法返回值效果list.sort() None直接把原列表按顺序排好。heapq.heapify(list) None直接把原列表调整成最小堆结构。
            heapq.heapify(self.mini_heap)
            
            # 3. 必须用 heappop 弹出最小的，直到剩下 k 个
            while len(self.mini_heap) > self.k_counts:
                #self.mini_heap.pop()。这只是列表的普通操作，它删掉的是列表的最后一个元素。但堆的最小元素在最前面（索引 0）
                heapq.heappop(self.mini_heap) # 这样才能保证弹出的是最小值

    #int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
    def add(self, val: int) -> int:
        #add and pop the smallest regardless, if val too small it wont matter

        #add (heappush) has no return val, require two input
        heapq.heappush(self.mini_heap, val)

        #now we do the same
        while len(self.mini_heap) > self.k_counts:
            heapq.heappop(self.mini_heap)
        
        #samllest of all k elements, is the k largeest in a given stream
        return self.mini_heap[0]
