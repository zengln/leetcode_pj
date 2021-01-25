# 升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
#
#
#  请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
#  示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5000
#  -10^4 <= nums[i] <= 10^4
#  nums 中的每个值都 独一无二
#  nums 肯定会在某个点上旋转
#  -10^4 <= target <= 10^4



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] <= nums[-1]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
        else:
            # 找到转变点
            mid = 0
            while left <= right:
                mid = (left + right) // 2
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    break
                elif nums[mid - 1] > nums[mid]:
                    mid = mid - 1
                    break
                elif nums[mid] > nums[-1]:
                    left = mid
                elif nums[mid] < nums[-1]:
                    right = mid - 1
            # 再找target
            if target > nums[-1]:
                left, right = 0, mid
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        right = mid - 1
                    elif nums[mid] < target:
                        left = mid + 1
            elif target <= nums[-1]:
                left, right = mid + 1, len(nums) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        right = mid - 1
                    elif nums[mid] < target:
                        left = mid + 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                #[left, mid],[mid + 1, right]
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                #[left, mid],[mid+1, right]
                if nums[mid] > nums[right]:
                    if nums[left] <= target <= nums[mid]:
                        right = mid
                    else:
                        left = mid + 1

        if nums[left] == target:
            return left

        return -1