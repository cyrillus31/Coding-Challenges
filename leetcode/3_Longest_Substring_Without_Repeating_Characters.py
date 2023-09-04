"""Given a string s, find the length of the longest 
substring without repeating characters.
 """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        result = ""
        rResult = ""
        start = 0 
        end = 0
        if len(s) == 0:
            return 0
        for index, letter in enumerate(s):

            if letter not in rResult:
                hashMap[letter] = index
                end = index + 1
            
            else:
                start = hashMap[letter]+1
                hashMap[letter] = index
                end = index + 1

            if end == len(s):
                end = None
            rResult = s[start:end]
            if len(rResult) >= len(result):
                result = rResult

        return len(result)
            
                



mySolution = Solution()
s = "abcabcbb"
print(mySolution.lengthOfLongestSubstring(s))

