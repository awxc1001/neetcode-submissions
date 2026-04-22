# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #      head -> next -> null
        #  prev(null) 《- head  next.copy(next)
        
        #treat head as head of unreversed list
        if head is None:
            return None
        #treat prev as the head of reversed list which 
        prev = None
        next_copy = None

        while head:
            next_copy = head.next
            head.next = prev
            prev = head
            head = next_copy

        #prev then becomes the tail node of orignal list
        #which is the head node of the reversed list
        #original head becomes null
        return prev

        