class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def trck(open, close):
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                trck(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                trck(open, close + 1)
                stack.pop()

        trck(0, 0)
        return res