# -*- coding:utf-8 -*-
# @Time    : 2021/1/6 16:59
# @Author  : zengln
# @File    : 归并排序.py


def mergesort(nums, start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    # 将数组分治
    # nums1
    mergesort(nums, start, mid)
    # nums2
    mergesort(nums, mid+1, end)
    # 将数组排序
    sort(nums, start, mid, end)


def sort(nums, start, mid, end):
    num1_index = start
    num2_index = mid + 1
    temp = []

    while num1_index <= mid and num2_index <= end:
        if nums[num1_index] < nums[num2_index]:
            temp.append(nums[num1_index])
            num1_index += 1
        else:
            temp.append(nums[num2_index])
            num2_index += 1


    if num1_index <= mid:
        temp += nums[num1_index:mid+1]

    if num2_index <= end:
        temp += nums[num2_index:end+1]


    for index in range(len(temp)):
        nums[start+index] = temp[index]


