class Solution:
    def reorderList(self, head: ListNode) -> None:
        stk = []
        # 先把所有节点装进栈里，得到倒序结果
        p = head
        while p is not None:
            stk.append(p)
            p = p.next

        p = head
        while p is not None:
            # 链表尾部的节点
            lastNode = stk.pop()
            next = p.next
            if lastNode == next or lastNode.next == next:
                # 结束条件，链表节点数为奇数或偶数时均适用
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next
            p = next