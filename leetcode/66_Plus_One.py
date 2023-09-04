"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
iNCREMEnt the large integer by one and return the resulting array of digits."""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = 0 
        carry = 0
        answer = []
        counter = 0
        for index, digit in enumerate(digits[::-1]):
            counter += 1
            if counter == 1:
                init = 1
            else:
                init = 0
            carry, result = divmod(digit+carry+init, 10)
            answer.append(result)
        if carry != 0:
            answer.append(carry)
        return answer[::-1]


print(Solution().plusOne([9,9,9,9,4]))
