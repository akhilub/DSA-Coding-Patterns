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


#Approach : Sorting +One pass traversal


#Considering the problem statement
'''
We can sort the intervals in ascending order by the left endpoint, and then traverse the intervals for merging operations.

The specific merging operation is as follows.

First, we add the first interval to the answer `ans`. Then, we consider each subsequent interval in turn:

If the right endpoint of the last interval in the answer array is less than the left endpoint of the current interval, it means that the two intervals will not overlap, so we can directly add the current interval to the end of the answer array;
Otherwise, it means that the two intervals overlap. We need to use the right endpoint of the current interval to update the right endpoint of the last interval in the answer array, setting it to the larger of the two.
Finally, we return the answer array.

The time complexity is O(n×logn), and the space complexity is O(logn). Here, n is the number of intervals.

'''



#TC :O(nlog(n))
#SC: O(log(n))

class Solution:
    def mergeInterval(self, intervals: List[List[int]]) -> List[List[int]]:        
        # 1)Sort Intervals:
        intervals.sort(key=lambda x:x[0])

        # 2)Initialization:
        ans=[intervals[0]]

        # 3)Iteration and Merging:
        for start,end in interval[1:]:
            lastEnd = ans[-1][1]

            if start <= lastEnd:
                ans[-1][1] = max(end,lastEnd)
            else:
                ans.append([start,end])
                
        return ans




#With Variation in Interval defination

# 1) Sort the interval based on start time to ensure a.start <=b.start
# 2) If a overlaps b (i.e b.start<=a.end) we need to merge them into new interval c such that
# c.start = a.start
# 3) c.end = max(a.end,b.end)
# 4) Repeat the above two steps to merge c with the next intervals if it overlaps with c


#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end

#  def print_interval(self):
#    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
  def merge(self, intervals):  

    intervals.sort(key = lambda x:x.start)
    
    ans = [intervals[0]]

    for interval in intervals[1:]:
      s = interval.start
      e = interval.end
      le = ans[-1].end

      if s<=le:
        ans[-1].end = max(ans[-1].end,e)
      else:
        ans.append(interval)
      
    return ans
