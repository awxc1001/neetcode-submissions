# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1 <= Length of the list <= 1000， head wont be None
        #just return when there is only one node
        if head.next is None:
            return 

        slow = head
        fast = head
        curr = head

        #step1, find mid using fast,slow and break into 2 lists
        #if no circle, fast will stop at last node or second last node
        #fast only move if two more nodes avaliable
        while fast.next and fast.next.next:
            #even, fast ends on second last node
            #odd, fast ends on last node
            fast = fast.next.next

            #but slow will always in middle
            #if odd, slow has one more node which is the middle node
            slow = slow.next

        #now break into two list
        l2_head = slow.next
        slow.next = None

        #step 2 now we reverse l2
        #l2_prev will be the new head of l2
        l2_prev = None

        while l2_head:
            temp = l2_head.next
            l2_head.next = l2_prev
            l2_prev = l2_head
            l2_head = temp
    

        #now we have the two lists
        head1 = curr
        head2 = l2_prev

        #we know l1 has more or equal nodes than l2
        #we while loop the shorter one to merge
        #avoid next empty
        while head2:
            #merge one by one
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            head2.next = temp1

            #move the head to another pair
            head1 = temp1
            head2 = temp2
        
        return 
            
        