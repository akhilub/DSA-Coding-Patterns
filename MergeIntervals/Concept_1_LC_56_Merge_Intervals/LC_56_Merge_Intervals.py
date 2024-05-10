# Lamda Function
# In python lambda functions are anonymous function that is defined without a name.
# We use `lambda` keyword instead of `def` to create it.
# lambda argument(s) :expression  #Syntax
# To sort the list based on the first index 
# we use list.sort(key = lambda x:x[0])   where list could be list = [[1,3],[8,10],[15,18],[2,6]]

#Vizulization

        
#            1   2       3         6        8        10          15        18
#        --------------------------------------------------------------------
#            |          |
#                |                 |        |         |          |          |


#Considering the problem statement
#Approach 

# 1) Sort the interval based on start time to ensure a.start <=b.start
# 2) If a overlaps b (i.e b.start<=a.end) we need to merge them into new interval c such that
# c.start = a.start
# 3) c.end = max(a.end,b.end)
# 4) Repeat the above two steps to merge c with the next intervals if it overlaps with c

class Solution:
    def mergeInterval(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        
        intervals.sort(key=lambda x:x[0])

        mergedInterval=[interval[0]]

        for start,end in interval[1:]:
            lastEnd = mergedInterval[-1][1]

            if start <= lastEnd:
                mergedInterval[-1][1] = max(end,lastEnd)
            else:
                mergedInterval.append([start,end])
        
        return mergedInterval

