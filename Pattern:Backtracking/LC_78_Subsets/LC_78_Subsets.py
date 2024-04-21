#nums = [1,2,3]
#
#           nums[i]
#            /   \
#          pick  skip
#


#Approach
#For each number we have two choices :include or skip in the subset
#Thus the total number of subsets is 2^N for N unique elements
#The following recursion is easy to understans.It takes two parameters the current subset and the ith number we are looking at now.
#The terminal condition of Recursion is that:
#     - when we reach the end (running out of numbers) we have one subset which we can copy to the list of anwsers 
#     - O/w we have two choices include this number or skip it
#And we can call the recursion backtracking respectively.



#As the Python uses Object-References when passing parameters the list (mutable ) is passed by Reference,
#we need to make a deep copy (using copy.deepcopy(cur) or cur[:]) to copy the current subset e.g cur to answer (list of all subsets)

# Syntax of Python Deepcopy
# Syntax: copy.deepcopy(x)

# Syntax of Python Shallowcopy
# Syntax: copy.copy(x)


class Solution:
    def subsets(self,nums):
        ans = []
        def backtrack(cur,i):
            if i == n:
                ans.append(cur[:])     #ans.append(copy.deepcopy(cur))  # cur[:] means deepcopy of 
                return 
            #pick
            backtrack(cur+[nums[i]],i+1)
            #skip
            backtrack(cur,i+1)

        backtrack([],0)
        return ans