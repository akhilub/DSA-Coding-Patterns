from typing import List

def find_array_quadruplet(nums: List[int], target: int) -> List[int]:
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                l,r = j+1,len(nums)-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s == target:
                        ans.add((nums[i],nums[j],nums[l],nums[r]))
                        return list(ans.pop())  # Convert the tuple to a list
                    elif s > target:
                        r-=1
                    else:
                        l+=1
        return []
    