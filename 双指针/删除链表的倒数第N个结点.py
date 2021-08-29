# -*- coding:utf-8 -*-
# @Time    : 2021/8/26 19:31
# @Author  : zengln
# @File    : 删除链表的倒数第N个结点.py

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#  进阶：你能尝试使用一趟扫描实现吗？
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  链表中结点的数目为 sz
#  1 <= sz <= 30
#  0 <= Node.val <= 100
#  1 <= n <= sz
#
#  Related Topics 链表 双指针
#  👍 1525 👎 0



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        index_slow = head
        index_fast = head
        last = None
        while index_fast.next:
            index_fast = index_fast.next

            if n == 1:
                last = index_slow
                index_slow = index_slow.next

            if n > 1:
                n -= 1

        print(index_slow)
        if index_slow == head:
            head = index_slow.next
        else:
            last.next = index_slow.next
        return head

