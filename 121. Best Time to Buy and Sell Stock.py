class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        best = 0
        for num in prices:
            if num < cheap:
                cheap = num
            if num - cheap > best:
                best = num - cheap
        return best
