# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        
        memo = {}
        
        def dp(i, weight):
            if i >= len(wt) or weight == 0:
                return 0
            if (i, weight) not in memo:
                if wt[i] <= weight:
                    memo[(i, weight)] = max(val[i] + dp(i + 1, weight - wt[i]), dp(i + 1, weight))
                else:
                    memo[(i, weight)] = dp(i + 1, weight)
            return memo[(i, weight)]
        
        return dp(0, W)