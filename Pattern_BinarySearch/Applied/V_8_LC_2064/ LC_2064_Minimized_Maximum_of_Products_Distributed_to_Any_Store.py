#Approach : Binary Search
#TC:O(nlog(max(quantities)))
#SC:O(1)


#Problem function is monotonically decreasing and we are looking for minimum
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def f(mid):             # f - numStores
            return sum((x+ mid-1) //mid for x in quantities)

        l , r = 1,max(quantities)

        while l<r:
            mid = (l+r)//2

            if f(mid)<=n:
                r = mid
            else:
                l = mid+1

        return l
    



'''
sum((x + mid-1) // mid for x in quantities)
        ||
        ||
sum( (x-1) // mid + 1 for x in qunatities)


'''

