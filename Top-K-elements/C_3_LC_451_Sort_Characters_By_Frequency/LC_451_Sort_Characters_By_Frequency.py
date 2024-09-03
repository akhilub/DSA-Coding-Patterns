#Approach :Heap(max-Heap)
#O(klogk) where k is the no of keys(distinct character of input string) in hashmap

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s) #character-freq map
        
        #add all characters to max-heap
        pq = []
        for ch,freq in cnt.items():
            heappush(pq,(-freq,ch))
            
        #Build a string,appending the most occuring characters first
        ans = [] #SortedString List
        while pq:
            freq , ch = heappop(pq)
            for _ in range(-freq):
                ans.append(ch)
                
            return ''.join(ans) 

'''
The time complexity of the above algorithm is O(DxlogD) where ‘D’ is the number of distinct characters in the input string. 
This means, in the worst case, when all characters are unique the time complexity of the algorithm will be O(N∗logN) where ‘N’ is the total number of characters in the string.
'''

#Competative Programming 
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s) #ch-fq map
        #building list of tuple based on ch-fq map sorted on the values in decreasing order 
        lst = sorted(cnt.items() ,key = lambda x:-x[1]) #Note sorted returns a list/array
        #join the ch based on their freq
        ans = ''.join(ch*fq for ch,fq in lst)
        return ans

'''
sorted(cnt.items() ,key = lambda x:-x[1])
                    ||
sorted(cnt.items() ,key = lambda x:x[1],reverse=True)
'''

#Python One-liner
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        return ''.join(ch*fq for ch,fq in sorted(cnt.items(), key=lambda x:-x[1]))
