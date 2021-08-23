# -*- coding:utf-8 -*-
# @Time    : 2021/8/23 19:11
# @Author  : zengln
# @File    : 旋转数组.py

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#
#
#  进阶：
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#
#
#
#
#  示例 1:
#
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 104
#  -231 <= nums[i] <= 231 - 1
#  0 <= k <= 105
#
#
#
#
#  Related Topics 数组 数学 双指针
#  👍 1080 👎 0



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * len(nums)
        index_nums = 0
        index_temp = k % len(nums)
        while index_nums < len(nums):
            if index_temp == len(nums):
                index_temp = 0
            temp[index_temp] = nums[index_nums]
            index_temp += 1
            index_nums += 1

        for i in range(len(temp)):
            nums[i] = temp[i]



