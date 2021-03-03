# -*- coding:utf-8 -*-
# @Time    : 2021/3/3 9:10
# @Author  : zengln
# @File    : 移动零.py

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


# 双指针, 移动法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = 0
        for index in range(len(nums)):
            if nums[index]:
                nums[num] = nums[index]
                num += 1

        for index in range(num, len(nums)):
            nums[index] = 0


# 快排思路
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1