"Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l


        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        
        # reverse whole array
        reverse(nums, 0, l-1)

        # reverse first k elements
        reverse(nums, 0, k-1)

        # reverse remaining elements
        reverse(nums, k, l-1)
