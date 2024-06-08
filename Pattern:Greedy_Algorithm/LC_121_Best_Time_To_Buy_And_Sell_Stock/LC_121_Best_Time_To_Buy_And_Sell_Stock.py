#Approach 1: Greedy DP
#We can enumerate each element of the prices array as the SP.Then we need to find a minimum value in front of it as the purchase price to maximize the profit
#Therefore we use a variable mi to maintain the prefix minimum value of the array prices
#Then we traverse the array prices for each element v , calculate the difference between it and the minimum value mi in front of it.
#And Update the answer to the maximum difference.Then update mi = min(mi,v).
#Continue to traverse the array prices until the traversal ends.Finally return the answer

#TC:O(n)
#SC:O(1)

#Python Language Concepts
'''
>>> import math
>>> a = math.inf
>>> a
inf

>>> x = float('-inf')
>>> y = float('inf')
>>> print(x < y)  # Output: True
True
>>>
>>> z = -math.inf
>>> x==z
True

'''

class Solution:
    def maxProfit(self,prices):
        ans,mi = 0 , math.inf
        for v in prices:
            mi = min(mi,v)
            ans = max(ans,v-mi)
        return ans



#Approch 2:

#Start from the beginning of the array, go to the end.
#Keep a global maxprofit 'ans'.
#Have a purchase price (which will be the price at the Oth index when you start the loop), for every price you encounter, calculate the profit and update maxprofit accordingly. If you find a price smaller than the purchase price, make that your purchase price and start calculating profit from then on w the new purchase price.
#In the end, youll have the maximum profit in the maxprofit variable. Solved in 1 pass.
#O(n). This is called Kadane's algorithm.

class Solution:
    def maxProfit(self,prices:List[int])-> int:
        if not prices: return 0
        
        ans = 0
        pre = prices[0]

        for i in range(1,len(prices)):
            pre = min(pre, prices[i])
            ans = max(ans, prices[i]-pre)

        return ans



