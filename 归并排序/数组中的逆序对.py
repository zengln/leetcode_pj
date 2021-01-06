# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#
#
#  示例 1:
#
#  输入: [7,5,6,4]
# 输出: 5
#
#
#
#  限制：
#
#  0 <= 数组长度 <= 50000

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        # 归并排序, 每次前面的数大于后面的数时,就是一次逆序对
        def sort(nums:List[int], start, mid, end):
            i = start
            j = mid+1
            temp = []

            while i<=mid and j<=end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    self.count += mid - i + 1
                    j += 1


            if i<=mid:
                temp += nums[i:mid+1]


            if j<=end:
                temp += nums[j:end+1]

            for index in range(len(temp)):
                nums[start+index] = temp[index]



        def cut(nums:List[int],start:int, end:int):

            if start >= end:
                return

            mid = (start+end)//2
            cut(nums, start, mid)
            cut(nums, mid+1, end)
            sort(nums,start,mid,end)


        cut(nums, 0, len(nums)-1)
        return self.count

# 冒泡算法时间超了
def reversePairs(self, nums: List[int]) -> int:
        # 冒泡算法，时间超过
        count = 0
        for num_index in range(1, len(nums)):
            temp = num_index
            while temp >= 1:
                if nums[temp] < nums[temp - 1]:
                    count += 1
                    temp_num = nums[temp]
                    nums[temp] = nums[temp-1]
                    nums[temp - 1] = temp_num
                else:
                    temp = 0

                temp -= 1
        return count
