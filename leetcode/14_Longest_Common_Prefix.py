"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = min(strs, key=lambda x: len(x))

        for word in strs:
            if prefix == "":
                return prefix

            length = len(prefix)
            if prefix in word[:length]:
                continue 

            else:
                while prefix != []:
                    prefix = prefix[:-1]
                    if prefix in word[:len(prefix)]:
                        break
        return prefix

mySolution = Solution()

print(mySolution.longestCommonPrefix(["morda", "moshka", "moskwa"]))
        

