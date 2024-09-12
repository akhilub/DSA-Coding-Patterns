## Description

Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

Example 1:
```
Input: nums1=[9, 8, 2], nums2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.
```

Example 2:
```
Input: nums1=[5, 2, 1], nums2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2]
```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 105`
- `-109 <= nums1[i], nums2[i] <= 109`
- `nums1 and nums2 both are sorted in non-decreasing order.`
- `1 <= k <= 104`
- `k <= nums1.length * nums2.length`