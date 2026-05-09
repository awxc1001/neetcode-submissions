"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #first time, create copy node and match each oringal node
        #借助哈希表把原始节点和克隆节点的映射存储起来
        if head is None:
            return None
        node_copies = {}
        #dont move head because we need to return head of copied
        curr = head

        while curr:
            node_copies[curr] = Node(curr.val)
            curr = curr.next

        #sceond time, loop original nodes and link the pointers to each copy node in the table, by locating them using orinal node as key
        p = head
        while p:
            #get of dict default returns None
            node_copies[p].next = node_copies.get(p.next)
            node_copies[p].random = node_copies.get(p.random)
            p = p.next
        
        #return the head of copied
        return node_copies[head]


        