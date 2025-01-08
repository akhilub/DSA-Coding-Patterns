#Approach:Simulation
'''
Store the id and timestamp of the logs as tuples in an array. 
Then in the retrieve() method, truncate the corresponding parts of start and end based on granularity, 
and traverse the array, adding the id that meets the conditions to the result array.

In terms of time complexity, the time complexity of the put() method is O(1), 
and the time complexity of the retrieve() method is O(n), where n is the length of the array.
'''

from typing import List
from collections import deque
class LogSystem:
    def __init__(self):
        self.logs = deque([])
        self.d = {
            "Year":4,
            "Month":7,
            "Day":10,
            "Hour":13,
            "Minute":16,
            "Seconsd":19
        }
    
    def put(self,id:int,timestamp:str)-> None:
        self.logs.appendleft((id,timestamp))        #O(1)
        
        
    def retrieve(self,start:str,end:str,granularity:str)->List[int]:
        i = self.d[granularity]
        logId = []
        for id,ts in self.logs:
            if start[:i]<=ts[:i]<=end[:i]:
                logId.append(id)
        
        return logId


'''

...
def __init__(self):
    self.logs = []
...

...
def put(self,id:int,timestamp:str)-> None:
    #self.logs.insert(0,(id,timestamp))         #O(n)
    #self.logs.append((id,timestamp))           #O(1)
...

'''        



'''
return [id for id ,ts in self.logs if start[:i]<=ts[:i]]<=end[:i]
                
                ||
            better than
                ||

logId = []
for id,ts in self.logs:
    if start[:i]<=ts[:i]<=end[:i]:
        logId.append(id)
return logId
'''
        
        
        
# Your LogSystem object will be instantiated and called as such:


obj = LogSystem()
#obj.put(id,timestamp)

obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")

#print(obj.logs)

# param_2 = obj.retrieve(start,end,granularity)
# Retrieve logs within the entire year of 2017
log = obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")
print(log)

# Retrieve logs from January 1, 2017
log = obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
print(log)

log = obj.retrieve("2017:01:01:00:00:00", "2017:01:01:23:59:59", "Day")
print(log)


'''
Time:
Constructor: O(1)
put(id: int, timestamp: str): O(1)
retrieve(start: str, end: str, granularity: str): O(n)
Space: 
O(|retrieve()|) -> O(n)
'''

#Explanation

'''
Attributes:
`self.logs:` A list that stores log entries, where each log entry is a tuple consisting of an id (integer) and a timestamp (string in the format YYYY:MM:DD:hh:mm:ss).
`self.d:` A dictionary mapping granularity names ("Year", "Month", "Day", "Hour", "Minute", "Second") to the index positions in the timestamp string that correspond to the end of each granularity level. 
These indices help in slicing timestamps up to the required granularity.


Methods:
`__init__(self)`

- Initializes the log system. It sets up the logs list to store the log entries and the d dictionary to map each granularity to its respective slice index in the timestamp strings.

`put(self, id: int, timestamp: str) -> None`

- Adds a log entry to the system. It appends a tuple containing the id and timestamp to the logs list. The id is an integer identifier for the log, and timestamp is a string representing when the log entry was made.


`retrieve(self, start: str, end: str, granularity: str) -> List[int]`

- Retrieves all log ids with timestamps that fall within the range from start to end, inclusive, at the specified granularity.
- The method uses the d dictionary to find the slice index i corresponding to the given granularity. This index determines how much of the timestamp strings should be considered for comparison.
- It then iterates over all stored logs, comparing the sliced timestamps (ts[:i]) against the sliced start and end boundaries.
- If a log’s timestamp falls within the range, the log’s id is included in the result list.
'''
