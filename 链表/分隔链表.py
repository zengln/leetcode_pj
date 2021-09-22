# -*- coding:utf-8 -*-
# @Time    : 2021/9/22 14:36
# @Author  : zengln
# @File    : 分隔链表.py

# 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
#
#  每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
#
#  这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。
#
#  返回一个由上述 k 部分组成的数组。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3], k = 5
# 输出：[[1],[2],[3],[],[]]
# 解释：
# 第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。
# 最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。
#
#
#  示例 2：
#
#
# 输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3
# 输出：[[1,2,3,4],[5,6,7],[8,9,10]]
# 解释：
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 1000]
#  0 <= Node.val <= 1000
#  1 <= k <= 50
#
#  Related Topics 链表
#  👍 183 👎 0



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1.算出链表长度
    2.根据长度算出每个部分的长度
    3.遍历链表，根据每部分长度截取链表
    """
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        if k >= length:
            result_length = [1] * length
            result_length += [0] * (k - length)
        else:
            s = length // k
            y = length % k
            result_length = [s] * k
            if y != 0:
                for i in range(y):
                    result_length[i] += 1
        result = []
        temp_length = 0
        temp = head
        index = 0

        while temp or index < len(result_length):
            if result_length[index] == 0:
                result.append(None)
                index += 1
                continue

            temp_list_node = temp
            temp = temp.next

            if temp_length == 0:
                result.append(temp_list_node)

            temp_length += 1
            if temp_length == result_length[index]:
                temp_list_node.next = None
                temp_length = 0
                index += 1

        return result




