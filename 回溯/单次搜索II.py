# -*- coding:utf-8 -*-
# @Time    : 2021/9/18 13:34
# @Author  : zengln
# @File    : 单次搜索II.py

# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。
#
#
#
#  示例 1：
#
#
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l"
# ,"v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
#  示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 12
#  board[i][j] 是一个小写英文字母
#  1 <= words.length <= 3 * 104
#  1 <= words[i].length <= 10
#  words[i] 由小写英文字母组成
#  words 中的所有字符串互不相同
#
#  Related Topics 字典树 数组 字符串 回溯 矩阵
#  👍 497 👎 0



class Solution:
    """
    思路：
    遍历矩阵每个点, 判断每个点是否为words里某个单次的开头字母
    如果是：那么开始上下左右遍历,同一次遍历已经使用过的字母需要标记，不能再次使用
    如果不是, 开始遍历下一个字母

    超时了，但是这种思路应该是正确的
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        def inner(x, y, word, tmp, result):
            for x, y in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                if 0 <= x < m and 0 <= y < n and len(tmp) <= len(word) and board[x][y] != '#':
                    temp_board = board[x][y]
                    temp = tmp + board[x][y]
                    board[x][y] = "#"
                    if temp == word:
                        if word not in result:
                            result.append(word)
                    elif len(temp) < len(word) and temp == word[:len(temp)]:
                        inner(x, y, word, temp, result)
                    board[x][y] = temp_board
        result = []
        for i in range(m):
            for j in range(n):
                for word in words:
                    if board[i][j] != word[0]:
                        continue
                    if board[i][j] == word:
                        if word not in result:
                            result.append(word)
                        continue
                    # 开始上下左右遍历
                    temp = board[i][j]
                    board[i][j] = '#'
                    inner(i, j, word, temp, result)
                    board[i][j] = temp

                for word in result:
                    if word in words:
                        words.remove(word)

        return result

