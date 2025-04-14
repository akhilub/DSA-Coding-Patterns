#Write this in interviews
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def f(mid):                     #f - numChildren is a function of candies
            return sum((c//mid) for c in candies)

        l, r = 1, max(candies)
        ans = 0
        while l <=r:
            mid = (l + r ) // 2
            if f(mid)>=k:
                ans = mid
                l = mid +1
            else:
                r = mid -1
        return ans
    

'''
We notice that if each child can receive v candies, then for any v' < v, each child can also receive v' candies. 
Therefore, we can use binary search to find the maximum v such that each child can receive v candies.
We define the left boundary of the binary search as l = 0 and the right boundary as r = max(candies), where max(candies) represents the maximum value in the array candies. 
During the binary search, we take the middle value mid = (l+r+1)//2 = ⌊(l+r+1)/2⌋ each time, and then calculate the total number of candies each child can receive. 

If the total is greater than or equal to k, it means each child can receive v candies, so we update the left boundary l = mid. 
Otherwise, we update the right boundary r = mid - 1. Finally, when l = r, we have found the maximum v.
The time complexity is O(nxlog M), where n is the length of the array candies, and M is the maximum value in the array candies. The space complexity is O (1).

'''




#Binary Search different than the regular one
#Problem function is monotonically decresing and we are looking for maximum
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def f(mid):                     #f - numChildren
            return sum((c//mid) for c in candies)

        l, r = 0, max(candies)
        while l<r:
            mid = (l + r +1) >> 1      #see deviation here from regular binary search
            if f(mid) >= k:
                l = mid                #see deviation here from regular binary search
            else:
                r = mid - 1            #see deviation here from regular binary search
        return l
    
'''
(l + r + 1) >> 1
    ||
    ||
(l+r+1)//2
    ||
    ||
(l+r)//2 + 1
    ||
    ||
ceil((l+r)/2)
'''