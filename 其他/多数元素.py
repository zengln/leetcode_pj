# -*- coding:utf-8 -*-
# @Time    : 2021/7/30 16:43
# @Author  : zengln
# @File    : 多数元素.py

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1：
#
#
# 输入：[3,2,3]
# 输出：3
#
#  示例 2：
#
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#
#
#
#
#  进阶：
#
#
#  尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
#
#  Related Topics 数组 哈希表 分治 计数 排序

"""
一次遍历，算出每个数据出现的次数
获取到 N/2
找到那个出现大于N/2的书
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = dict()
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1

        tmp = len(nums) // 2 + 1
        for key, value in count_dict.items():
            if value >= tmp:
                return key




