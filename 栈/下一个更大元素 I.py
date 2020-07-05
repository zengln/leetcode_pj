# -*- coding:utf-8 -*-
# @Time    : 2020/7/5 15:00
# @Author  : zengln
# @File    : 下一个更大元素 I.py
# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个
# 比其大的值。
#
#  nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
#
#
#
#  示例 1:
#
#  输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
#     对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
#     对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
#
#  示例 2:
#
#  输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#     对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
#
#
#
#
#  提示：
#
#
#  nums1和nums2中所有元素是唯一的。
#  nums1和nums2 的数组大小都不超过1000。
#
#  Related Topics 栈
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        for num in nums1:

            result = -1
            for j in range(len(nums2)-1, -1, -1):

                if nums2[j] == num:
                    if result == -1:
                        results.append(-1)
                    else:
                        results.append(nums2[result])
                    break

                if nums2[j] > num:
                    result = j

        return results

s = Solution()
print(s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
