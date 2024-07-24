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
#Approach : Sorting +One pass traversal

# 1) Sort the interval based on start time to ensure a.start <=b.start
# 2) If a overlaps b (i.e b.start<=a.end) we need to merge them into new interval c such that
# c.start = a.start
# 3) c.end = max(a.end,b.end)
# 4) Repeat the above two steps to merge c with the next intervals if it overlaps with c


#Algo

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
