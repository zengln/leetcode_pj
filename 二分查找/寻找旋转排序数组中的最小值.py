# -*- coding:utf-8 -*-
# @Time    : 2021/1/22 17:36
# @Author  : zengln
# @File    : 寻找旋转排序数组中的最小值.py

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
#
#  请找出其中最小的元素。
#
#
#
#  示例 1：
#
#
# 输入：nums = [3,4,5,1,2]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
#
#
#  示例 3：
#
#
# 输入：nums = [1]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5000
#  -5000 <= nums[i] <= 5000
#  nums 中的所有整数都是 唯一 的
#  nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转
#
#  Related Topics 数组 二分查找




class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[right] >= nums[0]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid - 1
