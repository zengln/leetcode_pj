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