- DFS + Branch-cutoff ---> Backtracking

- In backtracking we incrementally build a solution and follow the approach if the current solution can't take us to the valid solution, we abandon it and backtrack( go back) to try another solution



**Algorithmic technique**
Backtracking is an algorithmic technique for finding solutions to some computational problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

1. It has 6-7 main steps -
Implement a helper method usually named "backtrack" method.
2. The backtrack method takes a few parameters, common to many problems.
3. **Base case** - The backtrack method has a base case that defines when to add the temporary solution to the main result, and when to return.
4. **For-loop** - Most of the time we need a for-loop to iterate
through the input so that we can select a candidate one
by one.
5. **Select a candidate** - The first thing we do is choose a valid candidate.
6. **Explore the remaining problem** - Many times we use recursion, as we need to perform the same thing on the remaining problem. So, we recursively call the backtrack method.
7. **Remove the selected candidate** - We backtrack, remove the selected candidate and try other candidates.