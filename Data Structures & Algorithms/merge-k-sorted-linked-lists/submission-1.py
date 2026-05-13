# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    # val=0 和 next=None 是“救命”的默认值
    # 这样 ListNode(5) 或 ListNode(5, some_node) 都能跑通
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    #     想象堆内部是一个由这些节点组成的“金字塔”：
    # 当你把一个新节点放入堆底时，堆会问：“新节点 < 它的父节点吗？”
    # 如果你返回 True，堆就把新节点往上挪一层（交换位置）。

    # 堆会不停问，直到你返回 False（说明它不比父节点小了），或者它已经爬到了塔顶。
    # 这就是排序发生的过程： 堆通过无数次“两两询问 + 根据 True/False 交换位置”，最终确保了最小值永远待在最上面。
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        heap = []
        
        # 1. 初始化：先把每个链表的头放进去
        for head_node in lists:
            if head_node:
                heapq.heappush(heap, head_node)
                
        # 2. 循环：因为堆顶永远是最小的，所以每次弹出的都是当前全局最小
        while heap:
            smallest_node = heapq.heappop(heap)
            curr.next = smallest_node # 接入结果
            curr = curr.next
            
            # 3. 补位：谁出去了，谁的后面那个人就进来竞争
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
                
        return dummy.next
        