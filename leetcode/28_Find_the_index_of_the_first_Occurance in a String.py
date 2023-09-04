# Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        l = len(needle)
        for index in range(len(haystack)):
            
            if needle in haystack[index:index+l]:
                return index
            
        return (-1)