Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.


<p align ="center">
<img src = "/submissionImages/shapeArea.png"></img>
</p>

# Example

For `n = 2`, the output should be
`solution(n) = 5`;
For `n = 3`, the output should be
`solution(n) = 13`.


# Input/Output

- **[execution time limit] 4 seconds (py3)**

- **[memory limit] 1 GB**

- **[input] integer n**

  *Guaranteed constraints:*
  
  `1 ≤ n < 104.`

- [output] integer

   The area of the n-interesting polygon.
   

# Answer

           {     1 , i=1
    f(i) = {    f(i-1) + 4*i - 4 , $\forall$ i $\in$ {2,3,4,....,n}
           {