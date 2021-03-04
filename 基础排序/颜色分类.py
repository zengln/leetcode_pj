# -*- coding:utf-8 -*-
# @Time    : 2021/3/4 9:50
# @Author  : zengln
# @File    : 颜色分类.py

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
#  此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#
#
#  示例 2：
#
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：[0]
#
#
#  示例 4：
#
#
# 输入：nums = [1]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  1 <= n <= 300
#  nums[i] 为 0、1 或 2
#
#
#
#
#  进阶：
#
#
#  你可以不使用代码库中的排序函数来解决这道题吗？
#  你能想出一个仅使用常数空间的一趟扫描算法吗？
#
#  Related Topics 排序 数组 双指针

# 计数排序，不满足进阶要求
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            elif nums[i] == 1:
                one_count += 1
            elif nums[i] == 2:
                two_count += 1

        for i in range(len(nums)):
            if zero_count:
                nums[i] = 0
                zero_count -= 1
            elif one_count:
                nums[i] = 1
                one_count -= 1
            elif two_count:
                nums[i] = 2
                two_count -= 1