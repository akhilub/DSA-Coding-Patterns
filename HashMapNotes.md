```
----------------------------
|   Operation   |  TC      |
----------------------------
|   add()       |  O(1)    |
|   search()    |  O(1)    | 
|   insert()    |  O(1)    |
|   remove()    |  O(1)    |
----------------------------
```

# 3 Hash Map Applications in Coding Interviews


1. Pair Sum Problems

In these kind of problems, we can use a hashmap to check if the difference of a target and a number exists in an input list in O(1) time. 

This is an improvement over using an array, which would take us O(n) time.

How to check?

Use the value as the key and map it to its index. Loop over the list and check if our map contains the difference we are looking for.

```
class Solution:
    def twoSum(self,nums:List[int],target:int)-> List[int]:
        prevMap = {}  # val->index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[diff] = i
```

2. Duplicate Detection
   
Hash maps/sets are useful for detecting duplicates because of their fast O(1) lookup. Using an array, this could potentially be O(n) time.

This is particularly useful in graph problems when we want to avoid revisiting vertices.

How to check?

At each iteration, check if the current element is already in our hash map/set. If not, add, and move to the next iteration.

```
class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```


3. Counting

We can use the element as the key and map it to its frequency. 

This is useful in problems where we have to check if we have “enough” of something or problems where occurrences play a role like anagrams or counting wins and losses.

How to check?

Map each element (key) to its frequency (value), where the frequency is initially set to 0. If we encounter a key again, we retrieve its value and increment it by 1.

```
cnt = {}
for ch in s:
    cnt[ch] = cnt.get(ch,0)+1
```