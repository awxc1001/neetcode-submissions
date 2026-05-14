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
        #0 <= lists.length <= 1000
        if lists is None:
            return

        #有default value can skip params
        # dummy = ListNode(0, None)
        dummy = ListNode()
    
        #build from dummy
        curr = dummy
        
        min_heap = []

        #0 <= lists[i].length <= 100
        # ✅ 正确写法：必须判断非空
        for head_node in lists:
            if head_node: # 只有不为空的头节点才能进堆
                heapq.heappush(min_heap, head_node)
        
        while min_heap:
            smallest_node = heapq.heappop(min_heap)
            curr.next = smallest_node
            #put the new head in the heap if there is
            if smallest_node.next:
                heapq.heappush(min_heap, smallest_node.next)
            #move curr to next pointer
            curr = curr.next
        
        return dummy.next
        