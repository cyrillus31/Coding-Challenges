"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        opp = {"(": ")", 
                   "[": "]", 
                   "{": "}",
        }
        if len(s) % 2 != 0:
            return False
        stack = []
        for item in s:
            if opp.get(item):
                stack.append(item)
            else:
                if stack != [] and opp.get(stack.pop()) == item:
                    continue
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

my = Solution()
print(my.isValid("{([])}"))

                
