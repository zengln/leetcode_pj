# -*- coding:utf-8 -*-
# @Time    : 2021/9/8 13:40
# @Author  : zengln
# @File    : 三数之和.py

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
#  示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics 数组 双指针 排序

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp_nums = sorted(nums)
        for i in range(len(nums)-2):
            temp = temp_nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if temp + temp_nums[left] + temp_nums[right] == 0:
                    if [temp, temp_nums[left], temp_nums[right]] not in result:
                        result.append([temp, temp_nums[left], temp_nums[right]])
                    left += 1
                    right -= 1
                elif temp + temp_nums[left] + temp_nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result

