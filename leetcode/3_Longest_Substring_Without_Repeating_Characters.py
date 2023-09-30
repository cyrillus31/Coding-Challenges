"""Given a string s, find the length of the longest 
substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        elif len(s) == 1:
            return 1

        hash_table = {}
        left = 0
        left_letter = s[left]
        hash_table[left_letter] = left
        result = 1

        for right in range(1, len(s)):
            right_letter = s[right]
            if right_letter not in hash_table:
                hash_table[right_letter] = right
            else:
                prev = hash_table[right_letter]
                if prev < left:
                    pass
                else:
                    left = prev + 1
                hash_table[right_letter] = right
            length = right + 1 - left
            if length > result:
                result = length
            # print(left, right, length, s[left:right+1])
            # print(hash_table)

        return result


            

mySolution = Solution()
inputs = ("abcabcbb", "tmmzuxt", "aabaab!bb")

for result in map(mySolution.lengthOfLongestSubstring, inputs):
    print(result)

