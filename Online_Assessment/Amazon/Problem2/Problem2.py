from collections import Counter
from heapq import *

class Solution():
    #Solution using sorted function
    def arrayTransformations(self,nums):
        cnt = Counter(nums)
        sorted_tup = sorted(cnt.items() ,key = lambda x:(-x[1],x[0]))
        return [[num,fq] for num,fq in sorted_tup]
    
    
    
    #Using max-Heap
    def arrayTransformations(self,nums):
        cnt = Counter(nums)
        max_pq = []
        for num , fq in cnt.items():
            heappush(max_pq,(num,-fq))

        
        ans = []
        for _ in range(len(cnt.items())):
            num,fq = heappop(max_pq)
            ans.append([num,-fq])
            
        return ans
    
        
    def main():
        # Example arrays
        arr3  = [3, 3, 1, 2, 1]
        expected_output3 = [[1,2], [3, 2], [2, 1]]
        actual_output3 = Solution().arrayTransformations(arr3)
        
        arr1 = [4, 3, 5, 3, 1, 2, 1, 4, 3, 5, 7, 7, 7, 7, 7]
        expected_output1 = [[7, 5], [3, 3], [1, 2], [4, 2], [5, 2], [2, 1]]
        
        actual_output1 = Solution().arrayTransformations(arr1)
        
        arr2 = [1, 1, 2, 3, 3]
        expected_output2 = [[1, 2], [3, 2], [2, 1]]
        actual_output2 = Solution().arrayTransformations(arr2)
    
    
        print("Frequency Array 1:", actual_output1)
        print("Frequency Array 2:", actual_output2)
        print("Frequency Array 3:", actual_output3)


if __name__ == "__main__":
    Solution.main()
    
    