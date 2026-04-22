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
        #original head# Definition for singly-linked list.
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
        #original head becomes null# Definition for singly-linked list.
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
            
            # prev 可以直接从 None 变成指向 head，
            # 因为 prev = head 只是让变量 prev 保存和 head 一样的节点引用；
            # 这和 head.next = prev 是两件不同的事，前者改变量，后者改链表指向
            prev = head
            head = next_copy

        #prev then becomes the tail node of orignal list
        #which is the head node of the reversed list
        
        #orinal head 最后变成 None
        #原来的头节点那个节点对象还在，只是它已经变成反转后链表的尾巴了
        return prev

        
        return prev


        return prev
