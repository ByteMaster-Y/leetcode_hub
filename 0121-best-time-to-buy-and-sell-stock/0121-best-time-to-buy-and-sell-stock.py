class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 가장 저렴한 가격에 사서 (1) 가장 비싼 가격에 판다 (6) -> 차익 5
        if not prices and len(prices) < 2:
            return 0
        
        max_prices = 0
        min_prices = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            else:
                max_prices = max(max_prices, prices[i] - min_prices)

        return max_prices
