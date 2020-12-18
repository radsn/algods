# LC121: Best Time to Buy and Sell Stock
# only permitted at most one transaction (ie. one buy and one sell), design algorithm to find max profit

class Solution:
    def maxProfit(self, prices):
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# test
obj = Solution()
prices_1 = [7, 1, 5, 3, 6, 4]
prices_2 = [7, 6, 4, 3, 1]
print(obj.maxProfit(prices_1))
print(obj.maxProfit(prices_2))

# Goal is to find the largest peak following the smallest valley.
# BuyPrice needs to be before SellPrice -- track for minimum buy price
# Calculate profit for every element by subtracting minbuyprice -- track for max profit
# time: O(n) one pass | space: O(1)
