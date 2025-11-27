class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = [0] * n
        m = prices[0]
        pm = [0] * n
        for i in range(1,n):
            if prices[i] >= m :
                sell[i] = abs(prices[i] - m)
            pm[i] = max(pm[i-1] , sell[i])
            m = min(m , prices[i])
        # print(pm)
        # print(sell)
        buy = [0] * n
        mm = prices[-1]
        for i in range(n-2,-1,-1):
            if prices[i] <= mm :
                buy[i] = abs(prices[i] - mm)
            mm = max(mm , prices[i])
        # print(buy)
        ans = 0
        for i in range(n):
            ans = max(ans , buy[i]+pm[i])
        return ans