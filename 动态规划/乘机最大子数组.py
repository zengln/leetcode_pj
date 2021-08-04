# -*- coding:utf-8 -*-
# @Time    : 2021/8/4 15:46
# @Author  : zengln
# @File    : 乘机最大子数组.py

# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#
#
#  示例 1:
#
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
#  示例 2:
#
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#  Related Topics 数组 动态规划

class Solution:
    """
    负数不一定要舍弃，因为后面有负数，就等于正数。
    如果判断当前负数是否要舍弃？
    用两个数，一个存最大，一个存最小
    """
    def maxProduct(self, nums: List[int]) -> int:
        max_value = nums[0]
        pre_max = 1
        pre_min = 1
        for i in nums:
            temp_max = max(pre_max * i, pre_min * i, i)
            temp_min = min(pre_max * i, pre_min * i, i)
            pre_max = temp_max
            pre_min = temp_min
            max_value = max(max_value, pre_min, pre_max)
        return max_value

