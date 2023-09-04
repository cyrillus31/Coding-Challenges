# Given two binary strings a and b, return their sum as a binary string.
# BINARY ADDITION NEEDS TO BE CLEARER! REWORK FOR THE FUTURE!

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        if la > lb:
            b = b.zfill(la)
        else:
            a = a.zfill(lb)
        a = a[::-1]
        b = b[::-1]
        
        quotient = 0
        result = ""
        for index, number in enumerate(a):
            first = int(number)
            second = int(b[index])
            sum = first + second + quotient
            quotient, remainder = divmod(sum, 2)
            result =  str(remainder) + result
        
        result = (str(quotient) + result)
        if result == "00":
            return "0"
        else:
            result = result.lstrip("0")
        return result

mySolution = Solution()
print(Solution.addBinary(mySolution, "0", "0"))
