"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_copies = {}
        visited_create = set()

        if node is None:
            return None
        
        visited = set()
        #node with adjy of neigbors
        def dfs_create(node):
            if node is None:
                return
            
            #这里key in hashmap也可以当判断条件
            if node in visited:
                return
            
            #make current node and its copy with value only
            #we dont want to link orignal node for copies
            node_copies[node] = Node(node.val)
            visited.add(node)

            #create all the node of neighbors
            #mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
            # node.neighbors=[node2,node3]
            for neibo in node.neighbors:
                dfs_create(neibo)

        #now pointer the niegbors correctly
        #refresh visited
        visited1 = set()
        def dfs_pointneibo(node):
            if node is None:
                return
            
            if node in visited1:
                return
            
            visited1.add(node)

            #grab all the neibors of current node
            #use them to locate the neibos of copied node and link them
            for neibo in node.neighbors:
                #locate the copy
                neibo_copy = node_copies[neibo]

                #locate current and append into neibo list
                node_copies[node].neighbors.append(neibo_copy)
                dfs_pointneibo(neibo)

        dfs_create(node)
        dfs_pointneibo(node)

        return node_copies[node]











        

        
        