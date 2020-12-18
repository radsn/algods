#122: Best Time to Buy and Sell Stocks II -- complete as many transactions
class Solution(object):
    def maxProfit(self, prices):
        total = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                total += profit
        return total

#test:
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([1,2,3,4,5]))
print(obj.maxProfit([7,6,4,3,1]))

#Greedy: calculate profit between every consecutive transaction. Only if the profit>0, add into total.
#checking consecutively st anytime there is any profit, add into total.