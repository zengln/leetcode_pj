# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
#  字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。
#
#  示例 1:
#
#  输入: "3+2*2"
# 输出: 7
#
#
#  示例 2:
#
#  输入: " 3/2 "
# 输出: 1
#
#  示例 3:
#
#  输入: " 3+5 / 2 "
# 输出: 5
#
#
#  说明：
#
#
#  你可以假设所给定的表达式都是有效的。
#  请不要使用内置的库函数 eval。
#


class Solution:
    def calculate(self, s: str) -> int:
        stack_num = []
        num = 0
        operator = "+"
        s = s.strip()
        for index in range(0, len(s)):
            s_char = s[index]
            if s_char.isdigit():
               num = num * 10 + int(s_char)
               if index == len(s) - 1:
                   if operator == "*":
                       stack_num.append(stack_num.pop() * num)
                   elif operator == "/":
                       temp_num = stack_num.pop()
                       if temp_num < 0:
                           result = (0 - temp_num) // num
                           result = -result
                       else:
                           result = temp_num // num
                       stack_num.append(result)
                   elif operator == "-":
                       stack_num.append(-num)
                   else:
                       stack_num.append(num)
            elif s_char in ['+', '-', '*', '/']:
                if not stack_num:
                    stack_num.append(num)
                else:
                    if operator == "*":
                        stack_num.append(stack_num.pop() * num)
                    elif operator == "/":
                        temp_num = stack_num.pop()
                        if temp_num < 0:
                            result = (0 - temp_num) // num
                            result = -result
                        else:
                            result = temp_num // num
                        stack_num.append(result)
                    elif operator == "-":
                        stack_num.append(-num)
                    else:
                        stack_num.append(num)
                operator = s_char
                num = 0

        result = 0
        for num in stack_num:
            result += num
        return result



