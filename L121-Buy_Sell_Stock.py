L121 - Buy_Sell_Stock.py


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        for price in prices:
            lowest_price = price if price < lowest_price else lowest_price
            max_profit = (
                (price - lowest_price)
                if (price - lowest_price) > max_profit
                else max_profit
            )
        return max_profit


# time O(n) - go through prices once
# space O(1) - initialized two variables to keep track of lowest_price and max_profit
