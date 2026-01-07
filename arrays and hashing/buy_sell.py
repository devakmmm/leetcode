from typing import List
class Solution:
    def buyAndSellStock(self, prices: List[int]) -> int:
        cheaest=prices[0]
        max_profit=0

        for price in prices[1:]:
            if price<cheaest:
                cheaest=price
            max_profit=max(max_profit, price-cheaest)
        
        return max_profit
# Time Complexity: O(n)
# Space Complexity: O(1) since we are using constant space
# This function calculates the maximum profit that can be achieved from a list of stock prices by buying and selling once.
# It iterates through the list, keeping track of the cheapest price seen so far and the maximum profit that can be made.
