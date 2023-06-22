class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp=[[-1]*2 for _ in range(len(prices))]
        
        def buy_sell_with_fee(ind,buy):
            if ind==len(prices):
                return 0
            
            if dp[ind][buy]!=-1:return dp[ind][buy]
            
            profit=0
            
            if buy:
                profit=max(-prices[ind]+buy_sell_with_fee(ind+1,0),buy_sell_with_fee(ind+1,1))
                
            else:
                profit=max((prices[ind]-fee)+buy_sell_with_fee(ind+1,1),buy_sell_with_fee(ind+1,0))
            
            dp[ind][buy]=profit
            
            return profit
            
            
        return buy_sell_with_fee(0,1)
            
        
        