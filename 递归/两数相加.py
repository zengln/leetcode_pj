# -*- coding:utf-8 -*-
# @Time    : 2021/8/6 13:38
# @Author  : zengln
# @File    : 两数相加.py

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
#  请你将两个数相加，并以相同形式返回一个表示和的链表。
#
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
#  示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
#  示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
#  示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
#  提示：
#
#
#  每个链表中的节点数在范围 [1, 100] 内
#  0 <= Node.val <= 9
#  题目数据保证列表表示的数字不含前导零
#
#  Related Topics 递归 链表 数学
#  👍 6532 👎 0



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        计算方法 self.val + self.val + 进位
        l1 和 l2 长度不一致如何处理, 从前往后
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_sum(l1, l2, add):
            list_node = ListNode()
            if not (l1 or l2):
                if add:
                    list_node.val = add
                    list_node.next = None
                else:
                    list_node = None
                return list_node

            if not l1:
                l1 = ListNode()
                l1.val = 0
                l1.next = None
            l1_value = l1.val

            if not l2:
                l2 = ListNode()
                l2.val = 0
                l2.next = None
            l2_value = l2.val

            list_node.val = (l1_value + l2_value + add) % 10
            add = (l1_value + l2_value + add) // 10
            list_node.next = get_sum(l1.next, l2.next, add)
            return list_node

        return get_sum(l1, l2, 0)


