from typing import List  

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final_prices = []
        for i in range(len(prices)):
            discount_applied = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:         
                    final_prices.append(prices[i] - prices[j])
                    discount_applied = True
                    break
            if not discount_applied:
                final_prices.append(prices[i])
        return final_prices
    
s = Solution()
print(s.finalPrices(prices = [8,4,6,2,3]))
