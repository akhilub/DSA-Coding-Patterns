#Approach 2 
#Standard Backtrack DFS

'''
To find all permutations, we can use backtracking. 
We'll start with an empty list as our permutation. As we do backtracking, we’ll keep adding numbers to this list to build the permutation.

But we can not add the numbers that are already used in the permutation. 
So we need to track numbers that have been already used in the permutation.

For each unused number, we will append it to the current permutation and continue backtracking. 
When our permutation contains all the numbers, we add it to our answer and return.

The time complexity is O(n!), where n is the length of nums. 
This is because for n elements, we have n! possible permutations.
'''
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    used = [False] * len(nums)

    def dfs(path: List[int]) -> None:
      #if current permutation is complete
      if len(path) == len(nums):
        ans.append(path.copy())
        return

      #Try each number as next element
      for i, num in enumerate(nums):
        #Skip if number is used
        if used[i]:
          continue
        
        used[i] = True          #Add number to permutation
        path.append(num)

        dfs(path)               #Recurse with updated state

        path.pop()
        used[i] = False         #Remove number for next iteration

    #Call backtrack with initial state
    dfs([])
    return ans



'''

path.append(num)
dfs(path)
path.pop()
  
  ||
  ||

dfs(path+[num])

'''









































#Approach

#Recursive Backtrack
#1) We will keep one list(curSol) to keep the track of the element we visited in the nums
#2) Recursively we pass this list and keep on adding the elements that are different 
#3) Stopping condition is when we have reached the total length of array (nums) meaning there are no more permutation


#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self,nums):
        ans = []
        n =len(nums)

        def backtrack(curSol, i):
             # i tells the depth of the recursive call
            if i == n:
                ans.append(deepcopy(curSol))
                return 

            for ele in nums:
              if ele not in curSol:
                curSol.append(ele)
                backtrack(curSol,i+1)
                curSol.pop()

        backtrack([],0)
        return ans

