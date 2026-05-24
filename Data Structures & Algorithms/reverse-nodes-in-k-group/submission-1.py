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
        
        # 彻底告别 last_tail，改叫前组尾巴
        prev_group_tail = dummy
        
        # 4. 主循环：一组一组进行接力
        for _ in range(groups_to_reverse):
            # 告别 curr_group_start，改叫 old_head（反转前的旧头）
            # 比如第 1 轮时，它就是节点 1
            old_head = prev_group_tail.next
            
            # 调用辅助函数进行局部反转，返回新头部（比如节点 3）
            new_head = self.reverse_k_nodes(old_head, k)
            
            # 【全局缝合图示】：
            # 局部反转后，此时内部变成了： 3 -> 2 -> 1 -> 4 -> 5
            # 
            # 执行 prev_group_tail.next = new_head 后，前半部分顺利接通：
            # dummy -----------------> 3 -> 2 -> 1 -> 4 -> 5
            #   ^                      ^         ^
            # prev_group_tail       new_head   old_head
            prev_group_tail.next = new_head
            
            # 【交接棒图示】：
            # 这一组处理完了，原本的旧头（old_head，也就是节点 1）现在已经跑到这组的屁股后面了。
            # 下一轮循环时，它要留下来当挂钩，去勾住下一组的新头！
            # 执行 prev_group_tail = old_head 后：
            # dummy -> 3 -> 2 -> 1 -> 4 -> 5
            #                    ^
            #             prev_group_tail (老大哥移动到这里，为下一组反转做准备)
            prev_group_tail = old_head
            
        return dummy.next

    def reverse_k_nodes(self, node: ListNode, k: int) -> ListNode:
        # A. 探路：往后走 k 步，找到下一组的开头
        next_group_start = node
        for _ in range(k):
            next_group_start = next_group_start.next
            
        # B. 开始局部反转
        curr = node
        prev = next_group_start
        
        # 【局部反转逐帧变化】：
        # 初始状态：
        #   prev = 4
        #   curr = 1 -> 2 -> 3 -> 4...
        for _ in range(k):
            nxt = curr.next     # 1. 记住老二（nxt = 2）
            curr.next = prev    # 2. 老大反手指向 prev（1 -> 4）
            prev = curr         # 3. prev 往前挪（prev = 1）
            curr = nxt          # 4. curr 变成老二（curr = 2）
            
        # C. 循环了 k 次后，prev 刚好停在这一组反转后的“新头部”（节点 3）
        return prev