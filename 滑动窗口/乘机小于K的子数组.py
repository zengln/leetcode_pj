# -*- coding:utf-8 -*-
# @Time    : 2021/9/10 17:10
# @Author  : zengln
# @File    : 乘机小于K的子数组.py

# 给定一个正整数数组 nums和整数 k 。
#
#  请找出该数组内乘积小于 k 的连续的子数组的个数。
#
#
#
#  示例 1:
#
#
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
#
#
#  示例 2:
#
#
# 输入: nums = [1,2,3], k = 0
# 输出: 0
#
#
#
#  提示:
#
#
#  1 <= nums.length <= 3 * 104
#  1 <= nums[i] <= 1000
#  0 <= k <= 106
#
#  Related Topics 数组 滑动窗口
#  👍 288 👎 0

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        temp = 1
        left = 0
        result = 0
        for i in range(len(nums)):
            temp *= nums[i]
            while temp >= k:
                temp /= nums[left]
                left += 1
            result += (i - left + 1)
        return result



