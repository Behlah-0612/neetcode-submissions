class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,0
        profits = []
        for i in range(len(prices)): 
            buy = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] > buy :
                    sell = prices[j]
                    profits.append(sell-buy)
            print(buy, sell, profits)
            
        if len(profits) == 0:
            return 0
        else:
            return max(profits)



        