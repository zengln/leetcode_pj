# -*- coding:utf-8 -*-
# @Time    : 2021/9/7 15:40
# @Author  : zengln
# @File    : 寻找峰值.py

# 峰值元素是指其值大于左右相邻值的元素。
#
#  给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
#  你可以假设 nums[-1] = nums[n] = -∞ 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
#
#  示例 2：
#
#
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 1000
#  -231 <= nums[i] <= 231 - 1
#  对于所有有效的 i 都有 nums[i] != nums[i + 1]
#
#
#
#
#  进阶：你可以实现时间复杂度为 O(logN) 的解决方案吗？
#  Related Topics 数组 二分查找

class Solution:
    """
    先用二分法排序数组，返回最大值的index
    """
    def findPeakElement(self, nums: List[int]) -> int:
        result = 0
        temp = []
        for i in range(len(nums)):
            if not temp:
                temp.append(nums[i])
                result = i
                continue
            if nums[i] > temp[-1]:
                result = i
                temp.append(nums[i])
            elif nums[i] < temp[0]:
                temp.insert(0, nums[i])
            else:
                left = 0
                right = len(temp)
                while left < right:
                    mid = (left + right) // 2
                    if temp[mid] > nums[i]:
                        right = mid
                    else:
                        left = mid + 1
                temp.insert(left, nums[i])

        return result
