# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #case of empty or just one node
        if head is None:
            return
        
        
        #Remove the nth node from the end of the list
        #reverse the list first
        new_head = self.reverse_list(head)
        
        #incase first element got del, put a dummy
        dummy = ListNode(-1)
        curr = dummy
        curr.next = new_head

        steps = 0
        #stpes + 1 is equivlant to n
        while curr:
            #stop at the closest node before and perform 
            #del and connect
            if steps == n -1:
                #remove and link
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                #reverse again and return
                new_head = self.reverse_list(dummy.next)
                return new_head

            curr = curr.next
            steps += 1
    
    def reverse_list(self, head):

        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        
        return new_head
        

        