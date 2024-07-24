#Approach
#Nonoverlapping Conditions

#Condition 1
#                      start       end
#                       |           |                       |               |
#-------------------------------------------------------------------------------
#       |         |
# new_start     new_end

#Condition 2
#                                                   start       end
#                       |           |               |            |
#-----------------------------------------------------------------------------------
#                                                                        |         |
#                                                                   new_start     new_end

#Overlapping Condition
#Condition 3
#                      start       end
#                       |           |               |            |
#-----------------------------------------------------------------------------------
#                  |         |
#             new_start     new_end



class Solution:
    def insert(self,intervals:List[List[int]],newInterval:List[List[int]]):
        mergedInterval =[]
        for i in range(len(intervals)):
            new_start, new_end = newInterval[0], newInterval[1]
            start,end = interval[i][0],interval[i][1]

            if new_end<start:
                mergedInterval.append(newInterval)
                return mergedInterval + intervals[i:]

            elif end < new_start:
                mergedInterval.append(intervals)

            else:
                newInterval = [ min(new_start,start),max(end,new_end)]
            
        mergedInterval.append(newInterval)
        return mergedInterval


