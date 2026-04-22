class UF:
    def __init__(self, total_nodes):
        self.parent = list(range(total_nodes))
    
    def find_root(self, curr_node):
        #find the root node, which will have themself as the root node
        if self.parent[curr_node] != curr_node:
            #curr_node → parent → parent → parent → root
            self.parent[curr_node] = self.find_root(self.parent[curr_node])
        return self.parent[curr_node]
    
    def union(self, a, b):
        #root就是 index，对应某个节点
        #if ra == rb: 判断的是 a 和 b 是否在同一个集合（连通分量）里
        ra = self.find_root(a)
        rb = self.find_root(b)

        if ra == rb:
            return False

        self.parent[rb] = ra
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        total = n
        #union the two nodes in each edge
        for a,b in edges:
            if uf.union(a, b):
                total -= 1
        
        return total
        