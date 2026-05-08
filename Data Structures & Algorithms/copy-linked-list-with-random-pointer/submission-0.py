"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        originToClone = {}
        # 第一次遍历，先把所有节点克隆出来
        p = head
        while p:
            if p not in originToClone:
                originToClone[p] = Node(p.val)
            p = p.next
        
        # 第二次遍历，把克隆节点的结构连接好
        p = head
        while p:
            if p.next:
                originToClone[p].next = originToClone[p.next]
            if p.random:
                originToClone[p].random = originToClone[p.random]
            p = p.next
        
        # 返回克隆之后的头结点
        return originToClone.get(head)