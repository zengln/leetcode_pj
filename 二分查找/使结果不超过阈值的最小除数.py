# -*- coding:utf-8 -*-
# @Time    : 2021/2/9 10:24
# @Author  : zengln
# @File    : 使结果不超过阈值的最小除数.py

# 给你一个整数数组 nums 和一个正整数 threshold ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
#
#  请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
#
#  每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
#
#  题目保证一定有解。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,5,9], threshold = 6
# 输出：5
# 解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
# 如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
#
#
#  示例 2：
#
#
# 输入：nums = [2,3,5,7,11], threshold = 11
# 输出：3
#
#
#  示例 3：
#
#
# 输入：nums = [19], threshold = 5
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5 * 10^4
#  1 <= nums[i] <= 10^6
#  nums.length <= threshold <= 10^6
#
#  Related Topics 二分查找



import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        new_nums = sorted(nums)
        left, right = 1, new_nums[-1]
        while left < right:
            #[left,mid] [mid + 1, right]
            mid = (left + right) // 2

            sum = 0
            for i in nums:
                sum += math.ceil(i / mid)
                if sum > threshold:
                    break

            if sum > threshold:
                left = mid + 1
            else:
                right = mid
        return left
