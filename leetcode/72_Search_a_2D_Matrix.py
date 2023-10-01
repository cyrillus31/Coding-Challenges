"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    return True

                if target < arr[mid]:
                    right = mid - 1
                
                if target > arr[mid]:
                    left = mid + 1
            
            return False

        def binary_search_arrays(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                sub_arr = arr[mid]
                if sub_arr[0] <= target <= sub_arr[-1]:
                    return mid
                elif target < sub_arr[0]:
                    right = mid - 1
                elif target > sub_arr[-1]:
                    left = mid + 1
            return None

        sub_array_index = binary_search_arrays(matrix, target)
        if sub_array_index is not None:
            return binary_search(matrix[sub_array_index], target)
        else:
            return False 
