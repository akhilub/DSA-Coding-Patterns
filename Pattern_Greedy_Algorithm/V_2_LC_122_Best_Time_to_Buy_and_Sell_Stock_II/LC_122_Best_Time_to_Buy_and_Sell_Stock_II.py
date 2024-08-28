#Approach:Greedy Algorithm DP (Cumulative Max Profit Problem)

#TC:O(n) ,SC:O(1)

'''
Starting from the second day, if the stock price is higher than the previous day, 
buy on the previous day and sell on the current day to make a profit. 

If the stock price is lower than the previous day, do not buy or sell. 
In other words, buy and sell on all rising trading days, and do not trade on all falling trading days. 
The final profit will be the maximum.

Note the state of the i th day is only related to the state of the i- 1 th day. 
Therefore, we can use only two variables to maintain the state of the i — 1 th day, 
thereby optimizing the space complexity to O(1).
'''
class Solution:
    def maxProfit(self,prices):
        n = len(prices)
        ans = 0 # maxprofit
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                ans += prices[i]-prices[i-1]

        return ans

