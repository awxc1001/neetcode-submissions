class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use a min_heap to store the smallest distance on top and pop by k times
        mini_heap = []
        heapq.heapify(mini_heap)

        #distance to orign (0,0)
        #The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
        
        for point in points:
            x = point[0]
            y = point[1]
            #orign are 0 are 0 so dont care
            # distance = sqrt(x^2 + y^2)
            #this is correct sqrt and times
            distance = (x**2 + y**2) ** 0.5

            #add to mini_heap to rank
            #在 Python 算法中，看到“带权重的排序”或“根据 A 排 B”：
            #直接把 (权重, 数据) 丢进堆里。 注意：一定要把用于排序的那个数放在元组的第一个位置（索引 0）
            dist_tuple = (distance, point)
            heapq.heappush(mini_heap, dist_tuple)
        
        #answer want to us find the coordiantes
        #we pop the heap by k times to get k cloest points
        #1 <= k <= points.length <= 1000
        #-100 <= points[i][0], points[i][1] <= 100
        answers = []
        for _ in range(k):
            dist_tuple = heapq.heappop(mini_heap)
            answers.append( dist_tuple[1] )
        
        return answers

