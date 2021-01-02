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

'''
解题思路：

题目中给出，仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分

1. 运算满足先乘除后加减的原则
2. 遇到数字保存下来,如果是加减法不进行计算，直接入栈
3. 遇到乘除将结果计算出来后保留下计算出的数据入栈
4. 将栈中所有数据相加(减法也是一种加法，加上负数)

a.遍历整个字符串
b.如果是数字,保存在临时变量里
c.如果是符号,将临时变量入栈
d.符号为乘除, 当下次再遇到符号时,将栈顶元素与保存下来的变量进行运算
e.符号为加减, 当下次再遇到符号时,将变量入栈
d.遍历到最后一个元素时,再做一次(d、e判断)
'''

'''
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
'''

'''
# 第一版优化
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

            if index == len(s) - 1 or s_char in ['+', '-', '*', '/']:
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
'''
# 大佬与我解法的区别
# 1.
# 在进行除法时, 我使用//，这时如果是负数则会往后取值，所以我多做了一些判断
# 大佬的除法逻辑是，使用/，对结果进行取证,所以无需进行正负数的特殊区分
# 2.
# 返回时使用sum和手动计算的区别
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0; sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in '+-*/' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0; sign = s[i]
        return sum(stack)

'''

