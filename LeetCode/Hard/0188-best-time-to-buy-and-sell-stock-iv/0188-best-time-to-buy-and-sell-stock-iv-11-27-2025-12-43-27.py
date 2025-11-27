class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
            # if k == 1:
            #     left , right = 0,1
            #     ans = 0
            #     while right < len(prices) : 
            #         if prices[left] < prices[right] : 
            #             ans = max(ans , prices[right] - prices[left])
            #         else:
            #             left = right 
            #         right += 1
            #     return ans

            # if k == 2 :
            #     n = len(prices)
            #     sell = [0] * n
            #     m = prices[0]
            #     pm = [0] * n
            #     for i in range(1,n):
            #         if prices[i] >= m :
            #             sell[i] = abs(prices[i] - m)
            #         pm[i] = max(pm[i-1] , sell[i])
            #         m = min(m , prices[i])
            #     # print(pm)
            #     # print(sell)
            #     buy = [0] * n
            #     mm = prices[-1]
            #     for i in range(n-2,-1,-1):
            #         if prices[i] <= mm :
            #             buy[i] = abs(prices[i] - mm)
            #         mm = max(mm , prices[i])
            #     # print(buy)
            #     ans = 0
            #     for i in range(n):
            #         ans = max(ans , buy[i]+pm[i])
            #     return ans

            # n = len(prices) 
            # ans = 0 
            # a = []
            # for i in range(1,n):
            #     if prices[i] > prices[i-1] :
            #         ans += (prices[i] - prices[i-1]) 
            #         if a and a[-1][-1] == i-1 : 
            #             a[-1][0] += prices[i] - prices[i-1]
            #             a[-1][-1] = i
            #         else:
            #             a.append([prices[i] - prices[i-1] , i])
            # a.sort(key = lambda x : -x[0])
            # # print(ans,cnt)
            # # print(a)
            # if len(a) <= k : return ans
            # else:
            #     res = 0
            #     for i in range(k):
            #         res+= a[i][0]
            #     return res
        dp = {}
        def helper(i , buyOrSell , t_left,ans):
            if (i == len(prices)):
                return 0
            if (i , buyOrSell , t_left) in dp : return dp[(i , buyOrSell , t_left)]
            ans = helper(i+1 , buyOrSell , t_left ,ans)
            if (buyOrSell == 'buy' and t_left > 0 ):
                ans = max(ans , helper(i+1 , 'sell' , t_left , ans) - prices[i])
            elif (buyOrSell == 'sell'):
                ans = max(ans , helper(i+1 , 'buy' , t_left - 1 , ans) + prices[i])
            dp[(i , buyOrSell , t_left)] = ans
            return ans
        a = helper(0 , 'buy' , k , 0)
        return a