class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for num in nums:
            amount = d.get(num, 0)
            amount += 1
            d[num] = amount
        
        s = sorted(d, key=lambda x: d[x])
        return s[len(s)-k:]

