"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if lt != ls:
            return False
        
        ds = {}
        ts = {}
        for i in range(ls):
            letter_s = s[i]
            letter_t = t[i]
            if letter_s not in ds:
                ds[letter_s] = 1
            else:
                ds[letter_s] += 1
            
            if letter_t not in ts:
                ts[letter_t] = 1
            else:
                ts[letter_t] += 1
        
        return ds == ts
