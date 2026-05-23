class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        

        
        min_heap = []
        for num, freq in num_freq.items():
            tuple_info = (freq, num)
            min_heap.append(tuple_info)
        
        #heapify
        heapq.heapify(min_heap)

        #pop out all the small ones until only k elements left
        #which are the k highest freq
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        #append the num from the tuple to answer list
        ans = []
        for i in range(len(min_heap)):
            ans.append(min_heap[i][1])
        
        return ans
        

        
        
        

        