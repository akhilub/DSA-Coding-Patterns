#Approach:Bottom UP DP

'''
We define dp[i] as the maximum score that can be obtained starting from the i-th problem. Therefore, the answer is dp[0].
Considering dp[i], let the score of the i-th problem be p, and the number of problems to skip be b. 
If we solve the i-th problem, then we need to solve the problem after skipping b problems, 
thus dp[i] =p + dp[i + b + 1]. 
If we skip the i-th problem, then we start
solving from the (i + 1)-th problem, thus dp[i] = dp[i + 1]. 
We take the maximum value of the two. 

The state transition equation is as follows:
dp[i] = max(p + dp[i + b + 1],dp[i+1]) . 
We calculate the values of dp from back to front, and finally return dp[0] .
The time complexity is O(n), and the space complexity is O(n). Here, n is the number of problems.
'''



class Solution:
  def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        # dp[i] := the maximum points starting from questions[i]
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            points,brainPower = questions[i]
            nextIndex = i + brainPower +1
            nextPoints = dp[nextIndex] if nextIndex < n else 0
            dp[i] = max(points+nextPoints,dp[i+1])
        
        return dp[0]


#Approach: Top Down DP (Recursion +Memoization)
    

'''
We design a function dfs(i), which represents the maximum score that can be obtained starting from the i-th question. The answer is dfs(0).
The function dfsi) is calculated as follows:
• If i ≥ n, it means all questions have been solved, so return 0;
Otherwise, let the score of the i-th question be p, and the number of questions to skip be b. Then,
    dfs(i) = max(p + dfs(i +b+ 1), dfs(i +1)).
To avoid repeated calculations, we can use memoization by storing the values of dfs(i) in an array f.
The time complexity is O(n), and the space complexity is O(n), where n is the number of questions.

'''

#                                       question[i]
#                                        /     \
#                                       pick    skip
#                       existing points           points_from_question_skip
#                               + 
#               points_from_next_question_pick,
#                   
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i):
            if i>=len(questions):
                return 0

            p , bp = questions[i]
            #max(p + points_from_next_question_pick, points_from_question_skip)
            return max(p + dfs(i+bp+1),dfs(i+1))

        return dfs(0)
    


