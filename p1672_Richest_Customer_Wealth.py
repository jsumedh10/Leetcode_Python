# 1672. Richest Customer Wealth

# time - 49 seconds
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for cust in accounts:
            total = sum(cust)
            if total >= wealth:
                wealth = total
        return wealth 
       
      # Second solution - 55ms
      # return max([sum(cust) for cust in accounts])
