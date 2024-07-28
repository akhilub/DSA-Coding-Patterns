#Approach: Monotonic Queue

























#Sliding Window fixed length using two pointers
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