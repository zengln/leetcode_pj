# -*- coding:utf-8 -*-
# @Time    : 2021/1/27 13:57
# @Author  : zengln
# @File    : 搜索旋转排序数组II.py

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
#  编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
#  示例 1:
#
#  输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
#  示例 2:
#
#  输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
#  进阶:
#
#
#  这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。
#  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#




class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2

            if nums[mid] < nums[right]:
                # [left, mid -1],[mid, right]
                if nums[mid] <= target <= nums[right]:
                    if nums[mid] == target or nums[right] == target:
                        return True
                    left = mid
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                # [left, mid -1], [mid, right]
                if nums[left] <= target <= nums[mid - 1]:
                    if nums[left] == target or nums[mid - 1] == target:
                        return True
                    right = mid - 1
                else:
                    left = mid
            elif nums[mid] == nums[right]:
                if nums[right] == target:
                    return True
                else:
                    right = right - 1

        return False

