#Approach:Brute Force
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []
        for i in range(n):
            ans.append(prices[i])
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    ans[-1]-=prices[j]
                    break
        return ans
 
'''
ans[i]=prices[i]-prices[j]
        ||
        ||
        ||
ans[-1]-=prices[j]

'''



#Approach:Monotonic Stack

'''
The problem is essentially to find the first element on the right side that is smaller than each element. We can use a monotonic stack to solve this.

We traverse the array prices in reverse order, using the monotonic stack to find the nearest smaller element on the left side of the current element, and then calculate the discount.

The time complexity is O(n), and the space complexity is O(n). Here, n is the length of the array prices.
'''

#Using array value, traversing from n to 0
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []                        # an increasing stack
        ans = prices.copy()
        n = len(prices)
        for i in range(n-1,-1,-1):
            v = prices[i]
            while stk and stk[-1]>v:
                stk.pop()
            if stk:
                ans[i]=prices[i]-stk[-1]
            stk.append(v)
        return ans

'''
for i in reversed(range(n)):
            ||
        equivalent
            ||
for i in range(n-1,-1,-1):
'''

    
#Another way of writing monotonic stack ,This is more efficient
#Using array index, traversing from 0 to n
class Solution:
  def finalPrices(self, prices: list[int]) -> list[int]:
    stk = []                        # a decreasing stack
    ans = prices[::]
    n = len(prices)
    for i,v in enumerate(prices):
        # stack[-1] := i in the problem description.
        while stk and prices[stk[-1]]>=v:
            ans[stk.pop()]-=v
        stk.append(i)
    return ans


"""
ans[stk.pop()]-=v
    ||
    ||
    ||
idx = stk.pop()
ans[idx]=ans[idx]-v

"""