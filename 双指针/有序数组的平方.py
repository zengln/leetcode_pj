# -*- coding:utf-8 -*-
# @Time    : 2021/8/23 10:29
# @Author  : zengln
# @File    : 有序数组的平方.py

# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
#
#  示例 2：
#
#
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 104
#  -104 <= nums[i] <= 104
#  nums 已按 非递减顺序 排序
#
#
#
#
#  进阶：
#
#
#  请你设计时间复杂度为 O(n) 的算法解决本问题
#
#  Related Topics 数组 双指针 排序
#  👍 276 👎 0



class Solution:
    """
    两个指针分别从两头开始
    如果数组全是负数：那么nums[right]<0
    如果数组全是正数：那么nums[left]>0
    如果有正有负，则left是负数绝对值最大的数，right是正数最大的数，
    由于最终返回的结果是平方，所以可以直接拿绝对值做比较，算出新数组
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        index_left = 0
        index_right = len(nums) - 1
        result = []
        if nums[index_left] > 0:
            result = nums
        elif nums[index_right] < 0:
            result = nums[::-1]
        else:
            while index_left <= index_right:
                if abs(nums[index_left]) > nums[index_right]:
                    result.append(nums[index_left])
                    index_left += 1
                else:
                    result.append(nums[index_right])
                    index_right -= 1

            result = result[::-1]

        return [i * i for i in result]



