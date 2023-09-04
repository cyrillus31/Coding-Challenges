class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for element in nums:
            if element not in hash_set:
                hash_set.add(element)
            else:
                return True 
        return False 
