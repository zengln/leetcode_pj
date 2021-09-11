# -*- coding:utf-8 -*-
# @Time    : 2021/9/9 19:25
# @Author  : zengln
# @File    : 文本左右对齐.py

# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
#  说明:
#
#
#  单词是指由非空格字符组成的字符序列。
#  每个单词的长度大于 0，小于等于 maxWidth。
#  输入单词数组 words 至少包含一个单词。
#
#
#  示例:
#
#  输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
#
#  示例 2:
#
#  输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#
#
#  示例 3:
#
#  输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain
# ",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#
#  Related Topics 字符串 模拟


class Solution:
    """
    使用count计算当前行数的长度，使用temp临时保存每行的数据
    循环遍历单次列表
    当前行没数据时，将单次添加到temp中
    当前行存在数据时，在判断添加单词时，计算是否加上当前单次会超过最长限制，不超过则添加一个空格，再添加一个单次，
    count 加上单次长度与一个空格长度
    否则将最大长度减去count为当前行多余的个数，要分配到各个空格里去：
    当temp存在不止一个单词时，从1开始依次添加。
    当temp只存在一个单词时，全部添加在末尾，
    将当前行的数据添加到结果中，行数据清空，计数清空
    """
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        temp = []
        count = 0
        for word in words:
            if count == 0:
                # 如果是第一个单词, 直接添加
                temp.append(word)
                count = len(word)
                continue

            if count + len(word) + 1 <= maxWidth:
                temp.append(" ")
                temp.append(word)
                count += len(word)
                count += 1
            else:
                i = 0
                index = 1
                if len(temp) > 1:
                    while i < maxWidth - count:
                        if index >= len(temp):
                            index = 1
                        temp[index] += " "
                        i += 1
                        index += 2
                else:
                    temp.append(" " * (maxWidth - count))
                result.append("".join(temp))
                temp = [word]
                count = len(word)
        if temp:
            temp.append(" " * (maxWidth - count))
            result.append("".join(temp))
        return result




