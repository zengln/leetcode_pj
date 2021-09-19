# -*- coding:utf-8 -*-
# @Time    : 2021/9/10 13:47
# @Author  : zengln
# @File    : 长度最小的子数组.py

# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
#  找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
# 度。如果不存在符合条件的子数组，返回 0 。
#
#
#
#  示例 1：
#
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
#  示例 2：
#
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= target <= 109
#  1 <= nums.length <= 105
#  1 <= nums[i] <= 105
#
#
#
#
#  进阶：
#
#
#  如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
#
#  Related Topics 数组 二分查找 前缀和 滑动窗口
#  👍 758 👎 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        temp = []
        result = float(inf)
        temp_sum = 0
        for i in nums:
            temp.append(i)
            temp_sum += i
            if temp_sum < target:
                continue
            while temp_sum >= target:
                result = min(result, len(temp))
                temp_sum -= temp[0]
                temp.pop(0)
        return result

