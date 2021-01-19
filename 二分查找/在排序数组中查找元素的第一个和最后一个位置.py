# -*- coding:utf-8 -*-
# @Time    : 2021/1/19 11:38
# @Author  : zengln
# @File    : 在排序数组中查找元素的第一个和最后一个位置.py

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
#  如果数组中不存在目标值 target，返回 [-1, -1]。
#
#  进阶：
#
#
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
#  示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
#  示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 105
#  -109 <= nums[i] <= 109
#  nums 是一个非递减数组
#  -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        mid = 0
        left_flag, right_flag = True, True
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left > right:
            return [-1, -1]

        while left_flag or right_flag:
            if left - 1 > -1 and nums[left - 1] == target:
                left -= 1
            else:
                left_flag = False

            if right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
            else:
                right_flag = False

        return [left, right]


