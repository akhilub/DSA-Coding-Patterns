from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word using Counter
        cnt = Counter(words)
        
        # Step 2: Use a max-heap (simulated with negative frequencies) to store the words
        a = []
        for word,freq in cnt.items():
            heappush(a,(-freq,word))            # Push (-freq, word) to ensure the heap is ordered by frequency descending
                                                # and lexicographically ascending for words with the same frequency
        
        # Step 3: Extract the top k elements from the heap    
        ans = []
        for _ in range(k):
            _,word = heappop(a)    # Pop the word with the highest frequency (or lexicographically smallest if tie)
            ans.append(word)
        return ans
    


#Competative Programming
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        lst = sorted(cnt,key = lambda x:(-cnt[x],x))
        return lst[:k]
    
    
    
    
