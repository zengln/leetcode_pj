# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接
# 成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
#  求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
#
#  说明: 请尽可能地优化你算法的时间和空间复杂度。
#
#  示例 1:
#
#  输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
#
#  示例 2:
#
#  输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
#
#  示例 3:
#
#  输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def getMaxList(nums, num):
            drop = len(nums) - num
            result = []
            for temp in nums:
                while result and drop and result[-1] < temp:
                    result.pop()
                    drop -= 1

                result.append(temp)

            return result[:k]

        def merge(nums1, nums2):
            result = []
            while nums1 or nums2:
                bigger = nums1 if nums1 > nums2 else nums2
                result.append(bigger[0])
                bigger.pop(0)

            return result

        return max(merge(getMaxList(nums1, i), getMaxList(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))


