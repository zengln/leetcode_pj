# -*- coding:utf-8 -*-
# @Time    : 2021/2/5 14:05
# @Author  : zengln
# @File    : 转变数组后最接近目标值的数组和.py

# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和
# 最接近 target （最接近表示两者之差的绝对值最小）。
#
#  如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
#
#  请注意，答案不一定是 arr 中的数字。
#
#
#
#  示例 1：
#
#  输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
#
#
#  示例 2：
#
#  输入：arr = [2,3,5], target = 10
# 输出：5
#
#
#  示例 3：
#
#  输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 10^4
#  1 <= arr[i], target <= 10^5
#

class Solution:
    def sum(self, num, arr):
        sum_number = 0
        for index in range(len(arr)):
            if arr[index] < num:
                sum_number += arr[index]
            else:
                sum_number += num * (len(arr) - index)
                break
        return sum_number

    def findBestValue(self, arr: List[int], target: int) -> int:
        new_sort = sorted(arr)
        left, right = 1, new_sort[-1]

        while left < right:
            mid = (left + right) // 2
            #[left, mid][mid + 1, right]
            temp = self.sum(mid, new_sort)
            if temp < target:
                left = mid + 1
            else:
                right = mid

        if self.sum(right, new_sort) - target >= target - self.sum(right - 1, new_sort):
            return right - 1
        else:
            return right
