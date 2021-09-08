# -*- coding:utf-8 -*-
# @Time    : 2021/9/8 15:08
# @Author  : zengln
# @File    : 删除排序链表中的重复元素.py

# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
#  返回同样按升序排列的结果链表。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
#  提示：
#
#
#  链表中节点数目在范围 [0, 300] 内
#  -100 <= Node.val <= 100
#  题目数据保证链表已经按升序排列
#
#  Related Topics 链表 双指针


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    新建一个链表用于保存结果
    遍历原链表，当节点值不等于上一个节点值也不等于下一个节点值时，说明当前节点唯一，需要添加到结果链表中
    """

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        left = new_head
        right = head
        temp = None
        while right:
            if temp is None or temp.val != right.val:
                if right.next is None or right.val != right.next.val:
                    left.next = right
                    left = left.next
                temp = right

            right = right.next
            left.next = None
        return new_head.next
