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
        #   last_tail
        dummy = ListNode(0)
        dummy.next = head
        last_tail = dummy
        
        # 4. 主循环：一组一组进行接力
        for _ in range(groups_to_reverse):
            # 记录当前组的起点（反转前是 1，反转后 1 会变成这组的尾巴）
            curr_group_start = last_tail.next
            
            # 调用辅助函数进行局部反转，返回新头部
            new_head = self.reverse_k_nodes(curr_group_start, k)
            
            # 【全局缝合图示】：
            # 局部反转后，此时内部变成了： 3 -> 2 -> 1 -> 4 -> 5
            # 但上一组的尾巴 last_tail (dummy) 还没连上新头呢！
            #
            # 执行 last_tail.next = new_head 后：
            # dummy -----------------> 3 -> 2 -> 1 -> 4 -> 5
            #   ^                      ^         ^
            # last_tail             new_head  curr_group_start
            last_tail.next = new_head
            
            # 【交接棒图示】：
            # 这一组处理完了，现在的节点 1 (curr_group_start) 变成了下一轮的“上一组尾巴”
            # 执行 last_tail = curr_group_start 后：
            # dummy -> 3 -> 2 -> 1 -> 4 -> 5
            #                    ^
            #                last_tail (为下一组反转做准备)
            last_tail = curr_group_start
            
        return dummy.next

    def reverse_k_nodes(self, node: ListNode, k: int) -> ListNode:
        """
        局部反转辅助函数（自带逐帧动画注释）
        """
        # A. 探路：往后走 k 步，找到下一组的开头
        # 图示： 1 -> 2 -> 3 -> 4 -> 5 (k=3)
        #                      ^
        #               next_group_start
        next_group_start = node
        for _ in range(k):
            next_group_start = next_group_start.next
            
        # B. 开始局部反转
        curr = node
        # 核心：prev 初始化为下一组的开头（即 4），这样反转时尾巴自动就接上了！
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
            
            # ----------------------------------------------------
            # 第 1 次循环结束：
            #   未处理： 2 -> 3 -> 4... (这是 curr)
            #   已处理： 1 -> 4...      (这是 prev)
            # ----------------------------------------------------
            # 第 2 次循环结束：
            #   未处理： 3 -> 4...      (这是 curr)
            #   已处理： 2 -> 1 -> 4... (这是 prev)
            # ----------------------------------------------------
            # 第 3 次循环结束：
            #   未处理： 4 -> 5...           (这是 curr)
            #   已处理： 3 -> 2 -> 1 -> 4... (这是 prev)
            # ----------------------------------------------------
            
        # C. 循环了 k 次后，prev 刚好停在这一组反转后的“新头部”（节点 3）
        return prev