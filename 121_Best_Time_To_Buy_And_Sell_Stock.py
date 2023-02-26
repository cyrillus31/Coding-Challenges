class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        result = 0
        for price in prices:
            if price < low:
                low = price
            currentResult = price - low
            if currentResult > result:
                result = currentResult
        return result            






myprices = [7,1,5,3,6,4]
mysolution = Solution()

print(mysolution.maxProfit(myprices))