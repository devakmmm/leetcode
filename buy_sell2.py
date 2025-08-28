from typing import List
class Solution:
    def buyAndSellStock2(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0

        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit+=(profit[i]-profit[i-1]) 
#                 profit = 0
#                 values = [3, 5, 8]

#                  for i in range(1, len(values)):
#                       profit += values[i] - values[i-1]
#                       print(profit)



        return profit
    
    #we go through prices and find out profit each day could make by figuring out profit by adding it to difference btw lower price and higher
