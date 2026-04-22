class UF:
    def __init__(self , n):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]
    
    def union(self, a, b):
        ra, rb = self.find_root(a), self.find_root(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        self.count -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Tree in graph means no 无环 + 连通（uf.count == 1）。
        uf = UF(n)

        for edge in edges:
            a, b = edge[0], edge[1]
            if uf.union(a, b) is False:
                return False
            
            uf.union(a, b)
        
        #return only if UF count is 1, tree nodes all united in one set
        return uf.count == 1

            


        