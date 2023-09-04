"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space."""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            l = numbers[left]
            r = numbers[right]
            if (l+r) > target:
                right -= 1
            elif (l+r) < target:
                left += 1
            else:
                return left + 1, right + 1


"""
Explanation:
1. Establish two pointers: left and right. Left points to the smalles value in number, right points to the biggest.
2. Check the sum of the values those pointers point to.
3. If the sum is bigger than the target then the sum should be increased and the only way to do that is to increase the left pointer.
4. If the sum is smaller than the target then the sum should be decreased and the only way to do that is to decrease the right pointer.
5. Repeat that while left < right (we are guaranteed that the array has a single answer)
6. Before returning the answer increase the pointer by 1 since we have a 1-indexed array (which means the first element has index of 1 insead of 0)"""