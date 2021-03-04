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

# 冒泡排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

        return nums


# 选择排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            for i in range(index, len(nums)):
                if nums[i] < nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]

        return nums

# 插入排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for index in range(1, len(nums)):
            temp = nums[index]
            i = index - 1
            while i >= 0 and nums[i] > temp:
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = temp
        return nums


# 希尔排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        gap = len(nums) // 2
        while gap:
            for index in range(gap, len(nums)):
                temp = nums[index]
                index = index - gap
                while index >= 0 and temp < nums[index]:
                    nums[index + gap] = nums[index]
                    index -= gap

                nums[index + gap] = temp

            gap = gap // 2
        return nums


# 归并排序
def mergeSort(left, right):
    left_index = 0
    right_index = 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            result.append(right[right_index])
            right_index += 1
        elif left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1

    if left_index == len(left):
        result += right[right_index:]
    elif right_index == len(right):
        result += left[left_index:]

    return result


def MergeSort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    return mergeSort(MergeSort(left), MergeSort(right))


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return MergeSort(nums)

#快排
def quickSort(nums, left, right):
    if left >= right:
        return nums

    # 左右指针
    left_index = left
    right_index = right

    # 基准值
    temp = nums[left]

    pre_index = left_index

    while left_index < right_index:
        if pre_index == left_index and temp > nums[right_index]:
            nums[pre_index] = nums[right_index]
            pre_index = right_index
            left_index += 1
        elif pre_index == left_index and temp <= nums[right_index]:
            right_index -= 1
        elif pre_index == right_index and temp > nums[left_index]:
            left_index += 1
        elif pre_index == right_index and temp <= nums[left_index]:
            nums[pre_index] = nums[left_index]
            pre_index = left_index
            right_index -= 1

    nums[left_index] = temp

    quickSort(nums, left, left_index)
    quickSort(nums, left_index+1, right)

    return nums


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return quickSort(nums, 0, len(nums) - 1)