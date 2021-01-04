# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
#  说明：
#
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
#  示例：
#
#
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出：[1,2,2,3,5,6]
#
#
#
#  提示：
#
#
#  -10^9 <= nums1[i], nums2[i] <= 10^9
#  nums1.length == m + n
#  nums2.length == n

# 第一版
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    temp = []
    nums1_index = 0
    nums2_index = 0
    while nums1_index < m and nums2_index < n:
        if nums1[nums1_index] < nums2[nums2_index]:
            temp.append(nums1[nums1_index])
            nums1_index += 1
        elif nums1[nums1_index] > nums2[nums2_index]:
            temp.append(nums2[nums2_index])
            nums2_index += 1
        else:
            temp.append(nums2[nums2_index])
            temp.append(nums1[nums1_index])
            nums1_index += 1
            nums2_index += 1

    if nums1_index < m:
        temp += nums1[nums1_index:m]
    elif nums2_index < n:
        temp += nums2[nums2_index:n]

    for index in range(len(temp)):
        nums1[index] = temp[index]

#第二版，减少一次for循环,减少temp变量占用内存
def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m]
        nums1_index = 0
        nums2_index = 0
        index = 0
        while nums1_index < m and nums2_index < n:
            if temp[nums1_index] < nums2[nums2_index]:
                nums1[index] = temp[nums1_index]
                nums1_index += 1
            elif temp[nums1_index] > nums2[nums2_index]:
                nums1[index] = nums2[nums2_index]
                nums2_index += 1
            else:
                nums1[index] = nums2[nums2_index]
                index += 1
                nums1[index] = temp[nums1_index]
                nums1_index += 1
                nums2_index += 1
            index += 1

        if nums1_index < m:
            for temp_index in range(nums1_index, m):
                nums1[index] = temp[temp_index]
                index += 1
        elif nums2_index < n:
            for temp_index in range(nums2_index, n):
                nums1[index] = nums2[temp_index]
                index += 1


# 大佬同思路做法
# 清空nums1,后续直接append，这样可以不用记录当前需要替换nums1的哪个数据
# 相等的场景不额外使用一个分支

def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    # Make a copy of nums1.
    nums1_copy = nums1[:m]
    nums1[:] = []

    # Two get pointers for nums1_copy and nums2.
    p1 = 0
    p2 = 0

    # Compare elements from nums1_copy and nums2
    # and add the smallest one into nums1.
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # if there are still elements to add
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]


