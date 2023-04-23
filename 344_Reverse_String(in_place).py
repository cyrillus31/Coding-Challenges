"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory."""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

"""
Also consider:
s[:] = s[::-1]

Explanation:
s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the list inplace.
Under the hood, s[:] = is editing the actual memory bytes s points to, 
and s = points the variable name s to other bytes in the memory.
"""