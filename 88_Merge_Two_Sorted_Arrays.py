"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        pointer = m+n-1
        index1 = m-1
        index2 = n-1
        while index1 >= 0 and index2 >= 0:
            if nums2[index2] >= nums1[index1]:
                nums1[pointer] = nums2[index2]
                index2 -= 1
            else:
                nums1[pointer] = nums1[index1]
                index1 -= 1
            pointer -= 1
            print(nums1)
        while pointer >= 0 and index2 >= 0:
            nums1[pointer] = nums2[index2]
            pointer, index2 = pointer - 1, index2 - 1 
        print(f"RESULT: {nums1}")
        



my_solution = Solution()
my_solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
my_solution.merge([0], 0, [1], 1)
