class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        #times = [
        # [1,2,5],
        # [1,3,2],
        # [3,4,1]
        # ]
        # 建图以后 edges 变成：
        # {
        #  1: [(2,5), (3,2)],
        #  3: [(4,1)]
        # }
        # 意思就是：
        # 1 → 2 距离 5
        # 1 → 3 距离 2
        # 3 → 4 距离 1
        # 所以：
        # edges[1] = [(2,5),(3,2)]

        for time in times:
            u, v, t = time[0], time[1], time[2]
            #here is node, dist
            edges[u].append((v,t))
        
        #store (dist, node) into heap, dist at index 0 for sorting
        #different
        start_point = (0, k)
        mini_heap = []
        heapq.heappush(mini_heap, start_point)

        #djikstra weighted graph set for confirming mini_distance of each node 
        mini_confirm = set()
        #起点也必须通过 pop 来确认，push 它的邻居
        # mini_confirm.add(k)

        result = 0

        #peform bfs djikstra
        while mini_heap:
            #Dijkstra 只能一次 pop 一个节点，
            #每次 pop 就确认这个节点的最短距离，heap 自动保证 距离最小的先被处理。
            dist, cur_node = heapq.heappop(mini_heap)
            #BFS = “每层同时处理”，visited = “来过”
            # Dijkstra = “按最短距离处理”，visited = “最短距离已确认”
            # 起点也要经过 pop 才算确认，不然扩展邻居就错了
            if cur_node in mini_confirm:
                continue
            mini_confirm.add(cur_node)
            result = dist

            for neibo, neibo_dist in edges[cur_node]:
                if neibo not in mini_confirm:
                    heapq.heappush(mini_heap, (dist + neibo_dist, neibo))
            
        return result if len(mini_confirm) == n else - 1

        





