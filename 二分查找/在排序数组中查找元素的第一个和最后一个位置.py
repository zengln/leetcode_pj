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


class Solution:
    """
    先找到一个target，
    再以taget为界，分为两个数组
    分别再两个数组中找到初始与截止位置
    """


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if len(nums) == 0 or nums[left] > target or nums[right] < target:
            return [-1, -1]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = left = mid

        if nums[left] != target:
            return [-1, -1]

        temp_left = 0
        temp_right = left
        while temp_left < temp_right:
            mid = (temp_left + temp_right) // 2
            if nums[mid] < target:
                temp_left = mid + 1
            else:
                temp_right = mid

        start = temp_left
        temp_left = left
        temp_right = len(nums) - 1
        while temp_left < temp_right:
            mid = (temp_left + temp_right + 1) // 2
            if nums[mid] > target:
                temp_right = mid - 1
            else:
                temp_left = mid
        end = temp_left
        return [start, end]