# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/linked-list-cycle/
# 描述：
#       给定一个链表，判断链表中是否有环。
#       为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        a, b = head, head
        while a and b and b.next:
            a, b = a.next, b.next.next
            if a == b:
                return True
        return False