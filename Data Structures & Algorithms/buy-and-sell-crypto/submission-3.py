class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        # print(f"Valores iniciales: l {l}, r {r}")

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
           

        return maxProfit
