class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min_price = prices[0]

        for price in prices[1:]:
            maxprofit= max(maxprofit,price-min_price)
            min_price = min(min_price,price)

        return maxprofit