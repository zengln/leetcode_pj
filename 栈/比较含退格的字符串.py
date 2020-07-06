# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
#  注意：如果对空文本输入退格字符，文本继续为空。
#
#
#
#  示例 1：
#
#  输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
#
#  示例 2：
#
#  输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
#
#
#  示例 3：
#
#  输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
#
#
#  示例 4：
#
#  输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
#
#
#
#  提示：
#
#
#  1 <= S.length <= 200
#  1 <= T.length <= 200
#  S 和 T 只含有小写字母以及字符 '#'。
#
#
#
#
#  进阶：
#
#
#  用 O(N) 的时间复杂度和 O(1) 的空间复杂度
#
class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for s in S:
            if s != "#":
                stack_s.append(s)
            elif s == "#" and stack_s:
                stack_s.pop()

        for t in T:
            if t == "#" and stack_t:
                stack_t.pop()
            elif t != "#":
                stack_t.append(t)

        if ''.join(stack_s) == ''.join(stack_t):
            return True
        return False

# 进阶,抄的
import itertools

class Solution2(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

# 朴素的进阶实现
class Solution(object):
    def backspaceCompare(self, S, T):
        slen = len(S) -1
        tlen = len(T) -1
        while slen > -1 or tlen > -1:
            curS = ''
            curT = ''
            skip = 0
            tskip = 0
            while slen > -1 and not curS:
                if S[slen] != '#' and not skip:
                    curS = S[slen]
                elif S[slen] == "#":
                    skip += 1
                else:
                    skip -= 1
                slen -= 1

            while tlen > -1 and not curT:
                if T[tlen] != '#' and not tskip:
                    curT = T[tlen]
                elif T[tlen] == "#":
                    tskip += 1
                else:
                    tskip -= 1
                tlen -= 1

            if curS != curT:
                return False
        return True