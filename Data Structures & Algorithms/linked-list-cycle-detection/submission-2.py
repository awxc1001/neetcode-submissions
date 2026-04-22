# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 如果链表为空，或者只有一个节点且没有环，直接返回 False
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        # 只要快指针和它的下一步不为空，就继续跑
        while fast and fast.next:
            slow = slow.next          # 走 1 步
            fast = fast.next.next     # 走 2 步
            
            if slow == fast:          # “相遇”即有环
                return True
                
        return False
        