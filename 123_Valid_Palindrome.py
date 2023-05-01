"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def isalphanumeric(letter):
            if 97 <= ord(letter) <= 122 or 48 <= ord(letter) <= 57 or ord("A") <= ord(letter) <= ord("Z"):
                return True
            return False

        while left < right:
            if not isalphanumeric(s[left]):
                left += 1
                continue

            if not isalphanumeric(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1
        return True


s = Solution()
print(s.isPalindrome("0-P0"))
