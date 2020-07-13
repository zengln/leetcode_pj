# -*- coding:utf-8 -*-
# @Time    : 2020/7/13 20:15
# @Author  : zengln
# @File    : 扁平化嵌套列表迭代器.py

# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
#
#  列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
#
#
#
#  示例 1:
#
#  输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
#
#  示例 2:
#
#  输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

# 迭代
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.result = []
        self.index = 0

        def help(nestedList, result):
            for x in nestedList:
                if not x.isInteger():
                    help(x.getList(), result)
                else:
                    result.append(x.getInteger())

        help(nestedList, self.result)

    def next(self) -> int:
        tmp = self.result[self.index]
        self.index += 1
        return tmp

    def hasNext(self) -> bool:
        return len(self.result) != self.index


# 栈解法
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()


    def hasNext(self) -> bool:
        if len(self.stack) > 0 and self.stack[-1].isInteger() is False:
            self.stack.append(self.stack.pop().getList()[::-1])
        return len(self.stack) > 0