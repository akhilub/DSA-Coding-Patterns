from heapq import *

class Solution:
  def findKLargestPairs(self, nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
      return []
    
    pq = []
    for i in range(min(k, len(nums1))):
      heappush(pq, (-(nums1[i] + nums2[0]), i, 0))
    
    ans = []
    while pq and len(ans) < k:
      neg_sum, i, j = heappop(pq)
      ans.append([nums1[i], nums2[j]])
      if j + 1 < len(nums2):
        heappush(pq, (-(nums1[i] + nums2[j + 1]), i, j + 1))
    
    return ans

# Example usage:
solution = Solution()
nums1 = [10, 9, 8]
nums2 = [7, 6, 5]
k = 2
print(solution.findKLargestPairs(nums1, nums2, k))  # Expected Output: [[10, 7], [9, 7]]


nums1=[9, 8, 2]
nums2=[6, 3, 1]
K=3

print(solution.findKLargestPairs(nums1, nums2, K))