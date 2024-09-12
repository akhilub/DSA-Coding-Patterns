'''
Basically at any house `i` Robber have two options either to pick or skip

                                   f(i)
                                  /    \
                                 /      \    
                         H(i)+f(i-2)    f(i-1)
                           pick          skip
which boils down to    nums[i-1]+f(i-2)  f(i-1)

'''


'''
The circular arrangement means that at most one of the first and last houses can be chosen for theft, 
so this circular arrangement problem can be reduced to two single-row house problems.

The time complexity is O(n), where n is the length of the array. 
The space complexity is O(1).

'''



#No memory DP
class Solution:
    def rob(self, nums: List[int]) -> int:    
        n = len(nums)
        if n == 1:
            return nums[0]                # Only one house, rob it.
        if n == 2:
            return max(nums[0], nums[1])  # Two houses, rob the one with more money.
        
        # Helper function to perform linear robbing from start to end.
        def rob_linear(l: int, r: int) -> int:
            f0, f1 = 0, 0               # Two previous maximums
            for i in range(l, r+1):
                fi = max(f1, f0 + nums[i-1])
                f0,f1 = f1,fi
            return curr

        # Compute the maximum amount by excluding either the first or the last house
        # Case 1: Exclude the last house(rob from house 0 to n-2)
        case1 = rob_linear(0, n - 2)
        # Case 2: Exclude the first house(rob from house 1 to n-1)
        case2 = rob_linear(1, n - 1)
        
        # Return the maximum value obtained from both cases
        return max(case1, case2)