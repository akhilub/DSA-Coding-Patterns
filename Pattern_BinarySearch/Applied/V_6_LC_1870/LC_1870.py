# Approach:Binary Search
# Speed = Distance/Time
# Problem function f(time = distance/speed) is monotonically decreasing and we are looking for minimum speed
# on x-axis we have speed
# on y-axis we have time  = f(speed) = distance/speed 


# Time: O(nlog(M)),  where n and M are the number of train trips and the upper bound of the speed, respectively 
# here  M = r - l , r = 10^7 and l = 1
# Space: O(1)

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def check(speed):               #calculate time taken
            T = 0                       #total time
            for i, d in enumerate(dist[:-1]):
                T += ceil(d/speed) 
            return T + dist[-1]/speed
        
        
        L , R = 1 , int(1e7)+1          # L , R = 1 , 10**7
        ans = -1                        # initialize ans with impossible value
        while L<R:                      # while L<=R
            mid = (L+R)//2
            if check(mid)<=hour:
                ans = mid
                R = mid                 # R = mid -1
            else:
                L = mid+1
                
        return ans 
    
    
    
'''
def check(speed):               
    T = 0                       
    for i, d in enumerate(dist[:-1]):
        T += ceil(d/speed) 
    return T + dist[-1]/speed
    
    
    ||
equivalent
    ||
    
    
def check(speed):               
    T = 0                       
    for i, d in enumerate(dist):
        t = d/speed 
        T += ceil(t) if i!=len(dist)-1 else t
    return T 
    
    
'''