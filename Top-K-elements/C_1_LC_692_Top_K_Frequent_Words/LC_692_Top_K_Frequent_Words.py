#Logic:# Sort by frequency of words (in descending order) and then lexicographically (in ascending order)

'''
#MinHeap Approach doesnot work as expected because in 
#`heappush(pq,(freq,word))` freq first, default sort by 1st element
So do not go for it.
'''

#Appraoch :MaxHeap
#Write this in interviews
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word using Counter
        cnt = Counter(words)
        
        # Step 2: Use a max-heap (simulated with negative frequencies) to store the words
        pq = []
        for word,freq in cnt.items():
            heappush(pq,(-freq,word))           # Push (-freq, word) to ensure the heap is ordered by frequency descending
                                                # and lexicographically ascending for words with the same frequency
        
        # Step 3: Extract the top k elements from the heap    
        ans = []
        for _ in range(k):
            _,word = heappop(pq)    # Pop the word with the highest frequency (or lexicographically smallest if tie)
            ans.append(word)
        return ans
    









        

#Competative Programming
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        
        lst = sorted(cnt ,key = lambda x:(-cnt[x],x))    # multiple comparators "lambda x: (-cnt[x], x)"
        
        return lst[:k]


'''
Why the returned sorted() not a tuple (word, count), but only word?
it's the property of Counter() class
note we are passing `cnt` not `cnt.items()`



sorted(cnt,key = lambda x:(-cnt[x],x))

equivalent

sorted(cnt.keys(), key=lambda x: (-cnt[x], x))

'''



#Learn from below working concepts for how to use sorted the way you want it works

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        # Sort by frequency (in descending order) and then lexicographically (in ascending order)
        s_cnt = {w:f for w,f in sorted(cnt.items(),key = lambda x:(-x[1],x[0]))}
        
        return [w for w in s_cnt.keys()][:k]
    

'''
lst_of_tuple = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
'''
    
    
