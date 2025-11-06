class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_profit = 0
        current_profit = 0
        largest = 0
        smallest = prices[0]
        for i in prices:
            if i < smallest:
                smallest = i
                largest = 0
            elif i > largest:
                largest = i
            current_profit = largest - smallest
            if current_profit > best_profit:
                best_profit = current_profit
        return best_profit
