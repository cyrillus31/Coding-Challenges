"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def help(open_n, close_n):
            if open_n == close_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(") 
                help(open_n + 1, close_n)
                stack.pop()
            
            if close_n < open_n:
                stack.append(")")
                help(open_n, close_n + 1)
                stack.pop()
            
        help(0, 0) 
        return res
        
