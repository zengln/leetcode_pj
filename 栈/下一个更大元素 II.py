# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第
# 一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#
#  示例 1:
#
#
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
#
#
#  注意: 输入数组的长度不会超过 10000。

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for x in range(0, 2*len(nums)):
            while stack and stack[-1][0] < nums[x%len(nums)]:
                tmp = stack.pop()
                result[tmp[1]] = nums[x%len(nums)]

            stack.append([nums[x%len(nums)], x % len(nums)])
        return result


s = Solution()
print(s.nextGreaterElements([1, 4, 5, 1, 2]))

