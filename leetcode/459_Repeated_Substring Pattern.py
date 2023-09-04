# Given a string s, check if it can be constructed by taking a substring of it and 
# appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for index in range(len(s)-1):
            check = len(s) % (index+1) 
            if check == 0:
                division = len(s) / (index+1)
                if s[:index+1] * int(division) == s:
                    return True
                else:
                    continue
            else:
                continue
        return False