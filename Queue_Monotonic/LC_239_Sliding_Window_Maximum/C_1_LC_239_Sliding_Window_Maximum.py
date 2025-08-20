#Approach: Monotonic Queue

















#Approach:Heap(Priority Queue)

#1)Better/Stick to this approach, this is right 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Build max-heap using first k-1 elements
        pq = [] #max-heap
        for i in range(k-1):
            heappush(pq,(-nums[i],i))
        
        
        n = len(nums)
        ans = []
        for i in range(k-1,n):
            heappush(pq,(-nums[i],i))
            while pq[0][1] <= i-k:
                heappop(pq)
            ans.append(-pq[0][0])
        
        return ans 




#2)Wrong appraoch on the lower array slicing, this does not work because `i` again starts from 0 in slicied array start from k-1 to n
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Build max-heap using first k-1 elements
        pq = [] #max-heap
        for i , num in enumerate(nums[:k-1]):
            heappush(pq,(-num,i))
        
        
        ans = []
        for i , num in enumerate(nums[k-1:len(nums)]):     #Here indexing again starts from 0 for the sliced array nums[k-1:n]
            heappush(pq,(-num,i))
            
            while pq[0][1] <= i-k:
                heappop(pq)
            ans.append(-pq[0][0])
        
        return ans            
            

        
        



























#Approach: Sliding Window fixed length using two pointers
#TLE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            l = i
            r = i+k
            ans.append(max(nums[l:r]))
        return ans



#Sliding Window fixed length using dictionary
#TLE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        #Intialization
        cnt = Counter(nums[:k])
        mx = max(cnt)
        ans = [mx]
        for i in range(k,n):
            #add the incoming element from right
            cnt[nums[i]]+=1
            #subtract the outgoing element from left it is at position (right - k)
            cnt[nums[i-k]]-=1
            #apply conditions
            if cnt[nums[i-k]]==0:
                del cnt[nums[i-k]]  
            #update answer                    
            ans.append(max(cnt))
        return ans