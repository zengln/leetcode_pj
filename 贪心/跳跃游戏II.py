# -*- coding:utf-8 -*-
# @Time : 2021/8/2 13:27 
# @Author : zengln
# @File : 跳跃游戏II.py 
# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
#  假设你总是可以到达数组的最后一个位置。
#
#
#
#  示例 1:
#
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
#  示例 2:
#
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
#
#
#  提示:
#
#
#  1 <= nums.length <= 104
#  0 <= nums[i] <= 1000
#
#  Related Topics 贪心 数组 动态规划

class Solution:
    def jump(self, nums: List[int]) -> int:
        # max_step = [0] * len(nums)
        # for i in range(len(nums)):
        #     max_step[i] = i + nums[i]
        # print(max_step)
        # step = 0
        # jump = 0
        # while step < len(nums) - 1:
        #     step = max_step[step]
        #     jump += 1
        # return jump
        jump = 0
        start = 0
        end = 0
        max_step = 0
        # while end < len(nums)-1:
        #     max_step = 0
        #     for i in range(start, end, 1):
        #         if max_step < i + nums[i]:
        #             max_step = i + nums[i]
        #     start = end
        #     end = max_step
        #     jump += 1
        # return jump
        for i in range(len(nums)-1):
            if max_step < i + nums[i]:
                max_step = i + nums[i]

            if i == end:
                end = max_step
                jump += 1
        return jump



