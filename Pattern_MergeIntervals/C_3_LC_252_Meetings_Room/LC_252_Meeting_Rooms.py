from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals,key = lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
            return True
        



        
#Pythonic Way
# Learn about how all() ,any () and pairwise() works


from typing import List
from itertools import pairwise

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(a[1]<=b[0] for a,b in pairwise(intervals))    
    
    
 
 
 
 
from typing import List    
from itertools import pairwise
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        return not any(a[1] > b[0] for a,b in pairwise(intervals))
        # any is True, then conflict found   
        
        


        
#With Variation in interval defination

#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution2(object):
  def canAttendMeetings2(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    intervals = sorted(intervals, key=lambda x: x.start)
    
    for i in range(1, len(intervals)):
      if intervals[i-1].end > intervals[i].start:
        return False
    return True


        
        
        
        
        
        
        





if __name__=="__main__":
    intervals = [[0,30],[5,10],[15,20]]
    actual_output = Solution().canAttendMeetings(intervals)
    print(actual_output)
    
    
    intervals2 = [[7,10],[2,4]]
    actual_output2 = Solution().canAttendMeetings(intervals2)
    print(actual_output2)
    
    
    
    
    output1 = Solution2().canAttendMeetings2([Interval(0, 30), Interval(5, 10), Interval(15,20)])
    print(output1)