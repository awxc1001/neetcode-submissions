# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 算出链表总长度
        total_nodes = 0
        curr = head
        while curr:
            total_nodes += 1
            curr = curr.next
            
        # 2. 算出需要完整反转几组
        groups_to_reverse = total_nodes // k
        
        # 3. 建立哨兵节点 (Dummy Node)
        # 图示： dummy -> 1 -> 2 -> 3 -> 4 -> 5 (假设 k=3)
        #       ^
        #  prev_group_tail
        dummy = ListNode(0)
        dummy.next = head
        
        #locate the node that will be connect the reversed group head
        #first time is dummy
        node_before_reverse_group = dummy

        # 4. 主循环：一组一组进行接力
        for _ in range(groups_to_reverse):
            #find the reverse group start node
            reverse_start = node_before_reverse_group.next
            reverse_group_new_head, reverse_group_new_tail = self.reverse_k_nodes(reverse_start, k)

            #reassign the pointers
            node_before_reverse_group.next = reverse_group_new_head
            node_before_reverse_group = reverse_group_new_tail
        
        return dummy.next

    def reverse_k_nodes(self, node: ListNode, k: int):
        # 先往后往后走 k 步，定位到这组reverse后的next pointer
        reverse_group_next = node
        for _ in range(k):
            reverse_group_next = reverse_group_next.next
        
    # 1 -> 2 -> 3 ->4 -> 5 k =3
    # 4 is reverse_group_next
    # 5<- 4 <- 1 <- 2 <- 3
    #.                  
        #do the reverse with prev and curr, treat prev as the new head shifting
        curr = node
        prev = reverse_group_next
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #return as a tuple for the reversed group head and tail
        head_after_reverse = prev
        tail_after_reverse = node

        return head_after_reverse, tail_after_reverse



        
        

            
        