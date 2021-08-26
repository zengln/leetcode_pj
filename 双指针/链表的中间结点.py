# -*- coding:utf-8 -*-
# @Time    : 2021/8/26 19:12
# @Author  : zengln
# @File    : 链表的中间结点.py

# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#
#  如果有两个中间结点，则返回第二个中间结点。
#
#
#
#  示例 1：
#
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.
#
#
#  示例 2：
#
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#
#
#
#
#  提示：
#
#
#  给定链表的结点数介于 1 和 100 之间。
#
#  Related Topics 链表 双指针




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        index_slow = head
        index_fast = head
        count = 1
        while index_fast.next:
            index_fast = index_fast.next
            count += 1
            if count % 2 == 0:
                count = 0
                index_slow = index_slow.next

        return index_slow


