# -*- coding:utf-8 -*-
# @Time    : 2021/8/4 17:51
# @Author  : zengln
# @File    : 乘机为正数的最长子数组长度.py

# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
#
#  一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
#
#  请你返回乘积为正数的最长子数组长度。
#
#
#
#  示例 1：
#
#  输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
#
#
#  示例 2：
#
#  输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
#
#  示例 3：
#
#  输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
#
#
#  示例 4：
#
#  输入：nums = [-1,2]
# 输出：1
#
#
#  示例 5：
#
#  输入：nums = [1,2,3,5,-6,4,0,10]
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  -10^9 <= nums[i] <= 10^9
#
#  Related Topics 贪心 数组 动态规划
#  👍 44 👎 0

class Solution:
    """
    维护两个数组，一个表示当前乘机为正数时，最长子序列，一个为负数时，最长子序列
    正数： nums[i]>0
    dp[i] = dp[i-1]+1
    负数：
    dp_f[i] = dp_f[i-1]+1
    0：
    dp[i] = 0
    dp_f[i] = 0
    负数：
    dp[i] = dp_f[i-1]+1
    dp_f[i] = dp[i-1]+1
    """
    def getMaxLen(self, nums: List[int]) -> int:
        max_value = 0
        result = [0] * len(nums)
        result_f = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = 0
                result_f[i] = 0
            elif nums[i] > 0:
                result[i] = result[i-1] + 1
                if result_f[i-1] > 0:
                    result_f[i] = result_f[i-1] + 1
                else:
                    result_f[i] = 0
            elif nums[i] < 0:
                if result_f[i-1] > 0:
                    result[i] = result_f[i-1]+1
                else:
                    result[i] = 0
                result_f[i] = result[i-1] + 1
            # print(result, result_f)
            max_value = max(max_value, result[i])
        return max_value


