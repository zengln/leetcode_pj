# -*- coding:utf-8 -*-
# @Time    : 2021/2/23 9:49
# @Author  : zengln
# @File    : 排序数组.py

# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
#  示例 1：
#
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  -50000 <= nums[i] <= 50000
#

# 二分法排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if not result:
                result.append(i)
            else:
                left, right = 0, len(result)
                while left < right:
                    mid = (left + right) // 2
                    if result[mid] >= i:
                        right = mid
                    elif result[mid] < i:
                        left = mid + 1

                if left == len(result):
                    result.append(i)
                else:
                    result.insert(left, i)

        return result