class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None:
            return -1
        
        #python only has min_heap so conver negative
        neg_nums = [-x for x in nums]

        # convert to a heap (修正：heapify 是原地修改，直接作用于 neg_nums)
        heapq.heapify(neg_nums)
        heap = neg_nums

        #pop out k-1 elements and the kth largest element is top of the heap
        counter = 0
        while heap and counter < k-1:
            heapq.heappop(heap)
            counter +=1

        kth = heapq.heappop(heap)
        #covert back to correct sign
        return -kth

        