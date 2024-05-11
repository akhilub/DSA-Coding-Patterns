#Approach : HashTable

#We can use the hash table `seen` to store the array value and the corresponding subscript.

#Traverse the array `nums`, when you find `target - nums[i]` in the hash table, it means that the target value is found, and the index of `target - nums[i]` and `i` are returned.

#The time complexity is O(n) and the space complexity is O(n). Where n is the length of the array nums.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {} #map elements with their indexs {ele:idx}
    for idx,ele in enumerate(nums):
        num = target - ele
        if num in seen:
            return [seen[num],idx]
        seen[ele] = idx
