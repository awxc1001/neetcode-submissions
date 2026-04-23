# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy

        #l1 len == l2 len
        head1 = l1
        head2 = l2

        #to carry to next node pari calculation
        carry_val = 0

        ## 【改动点】只要有人没走完，就不能停
        while head1 or head2:
            
            #for uneven size list
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0

            #0 <= Node.val <= 9, so max is 9 + 9 + carry_value(1 if before has sum over 10) = 19
            node_sum = val1 + val2 + carry_val
            curr_val = node_sum % 10
            carry_val = node_sum // 10

            #make node and append to new list
            node = ListNode(curr_val)
            curr.next = node

            #update pointers
            curr = curr.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        #add the leftover carry_val to end of new list
        if carry_val != 0:
            node = ListNode(carry_val)
            curr.next = node
        
        return dummy.next
