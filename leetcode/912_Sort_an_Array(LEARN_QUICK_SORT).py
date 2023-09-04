"""Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n))
 time complexity and with the smallest space complexity possible.
 """

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def qsort(nums):
            if len(nums) < 2:
                return nums

            pivot = nums[-1]
            less = [num for num in nums if num < pivot]
            more = [num for num in nums if num > pivot]
            return qsort(less) + [pivot] + qsort(more)
        return qsort(nums)

my_solution = Solution()
arr = [1,43,5243,563,43,235,132,43,43,2,3]
print(my_solution.sortArray(arr))
