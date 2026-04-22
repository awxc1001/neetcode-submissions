# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #making new list require a dummy as head to avoid nothing at begin
        #of the list, edege case
        
        #leave as it is, we turn dummy.next as the head of new list
        dummy = ListNode(-1)

        #use a current pointer tag to loop down and construct
        curr = dummy

        #use pointers to point head of the two lists
        head1 = list1
        head2 = list2

        #now merge l1 and l2
        while head1 and head2:
            if head1.val < head2.val:
                #form the new link
                curr.next = head1
                #break the old one
                head1_next_copy = head1.next
                head1.next = None
                head1 = head1_next_copy
                #curr move foward
                curr = curr.next
            else:
                curr.next = head2
                head2_next_copy = head2.next
                head2.next = None
                head2 = head2_next_copy
                curr = curr.next

        #append the leftover one
        if head1:
            curr.next = head1
        if head2:
            curr.next = head2
        
        return dummy.next

