# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
#  示例 1:
#
#  输入: 121
# 输出: true
#
#
#  示例 2:
#
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
#  示例 3:
#
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
#  进阶:
#
#  你能不将整数转为字符串来解决这个问题吗？



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = 0
        temp = x
        while temp != 0:
            result = result * 10 + temp % 10
            temp //= 10

        return True if result == x else False

# 遍历一半x的解法
'''
                if x < 0 or (x % 10 == 0 and x != 0):
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            x //= 10

        return True if result == x or result // 10 == x else False
'''

# 字符串解法
'''
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        num = x_str.__len__()
        return True if x_str[:num//2] == x_str[::-1][:num//2] else False
'''

