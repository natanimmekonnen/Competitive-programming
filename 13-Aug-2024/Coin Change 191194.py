# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
    
        def dp(n):
            
            if n == 0:
                return 0
            if n < 0:
                return -1
            
            
            if n in memo:
                return memo[n]
            
            
            min_coins = float('inf')
            
            
            for coin in coins:
                res = dp(n - coin)
                if res >= 0: 
                    min_coins = min(min_coins, res + 1)
            memo[n] = min_coins if min_coins != float('inf') else -1
            return memo[n]
        
        return dp(amount)
        
            