class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        running_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                running_profit += prices[i] - prices[i - 1]
        return running_profit


if __name__ == "__main__":
    assert Solution().maxProfit([7,1,5,3,6,4]) == 7
    assert Solution().maxProfit([1,2,3,4,5]) == 4
