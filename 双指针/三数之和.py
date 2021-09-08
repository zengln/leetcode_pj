# -*- coding:utf-8 -*-
# @Time    : 2021/9/8 13:40
# @Author  : zengln
# @File    : 三数之和.py

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
#  示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics 数组 双指针 排序

class Solution:
    """
    数组先排序, 排序完成后再使用双指针找到另外另个数
    再将结果加入之前，先判断是否已经存在相同结
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp_nums = sorted(nums)
        for i in range(len(nums)-2):
            temp = temp_nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if temp + temp_nums[left] + temp_nums[right] == 0:
                    if [temp, temp_nums[left], temp_nums[right]] not in result:
                        result.append([temp, temp_nums[left], temp_nums[right]])
                    left += 1
                    right -= 1
                elif temp + temp_nums[left] + temp_nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result

   """
    因为先排序了所以第一个数大于0后，后面两个数必定大于0，没有必须再继续，直接返回
    当第一个数遍历时，与上一个数相等，直接跳过这个数避免重复结果
    while里两个指针也是类似，当left的值与left+1的值相等时，找到第一个不等于left的值
    right的值与right-1相等时，找到第一个不等于right的值
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp_nums = sorted(nums)
        # print(temp_nums)
        for i in range(len(nums) - 2):
            temp = temp_nums[i]
            if temp > 0:
                return result
            if i > 0 and temp_nums[i] == temp_nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if temp + temp_nums[left] + temp_nums[right] == 0:
                    result.append([temp, temp_nums[left], temp_nums[right]])
                    while left < right and temp_nums[left] == temp_nums[left + 1]:
                        left += 1
                    while left < right and temp_nums[right] == temp_nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif temp + temp_nums[left] + temp_nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result