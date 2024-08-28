# Approach Greedy Algorithm
'''
We can use a variable `mx` to record the farthest position that can be reached from the current position, a variable `last` to record the position of the last jump, and a variable ``ans`` to record the number of jumps.
Next, we traverse each position i in [0,..n - 2]. For each position i, we can calculate the farthest position that can be reached from the current position through i + nums[i]. We use `mx` to record this farthest position, that is, mх = max (mx, i + nums i]). Then, we check whether the current position has
reached the boundary of the last jump, that is, i == last. If it has reached, then we need
to make a jump, update last to mx, and increase the number of jumps `ans` by 1.
Finally, we return the number of jumps `ans`.
The time complexity is O(n), where n is the length of the array. 
The space complexity is 0(1).

'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        mx=last=ans=0
        # stop at 2nd-to-last, not the last index.
        # because, eg. nums=[1,0] or nums=[0,0],
        # just check the 2nd-to-last then we can decide if able to reach end

        # eg. - if input is [0], then 0 step needed
        for i in range(len(nums)-1):
            mx=max(mx,i+nums[i])
            
            if i==last:
                last = mx # update last before if check
                ans+=1    # in question, guarenteed can reach end. or else need more check

        return ans

