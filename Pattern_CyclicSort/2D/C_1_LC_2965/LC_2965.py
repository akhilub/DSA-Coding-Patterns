#Approach:2D Cyclic Sort
#TC:O(n²)
#SC:O(1)

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)                           # no of rows/lists
        n = len(grid[0])                        # no of cols/items in each list
        r = 0                                   # to traverse rows/lists:
        while r<m:
            c = 0                               # to traverse cols/each list
            while c<n:
                correct_r, correct_c = (grid[r][c] - 1) // m, (grid[r][c] - 1) % n          
                if grid[r][c] != grid[correct_r][correct_c]:
                    grid[r][c], grid[correct_r][correct_c] = grid[correct_r][correct_c], grid[r][c]
                else:
                    c+=1
            r+=1
        
        
        rep , miss = 0,0                    #rep - repeating number , miss - missing number
        for i in range(m):
            for j in range(n):
                num = i * m + j + 1         #num - create number from 1 to n²
                
                if grid[i][j]!=num:
                    rep = grid[i][j]
                    miss = num
                    
        return [rep,miss]
    



'''
correct_r, correct_c = (grid[r][c] - 1) // m, (grid[r][c] - 1) % n

                    ||
                since m==n
                    ||

correct_r, correct_c = divmod(grid[r][c] - 1, n)
'''
    
    
    
#Competative Programming
#Approach:Counting

'''
We create an array `cnt` of length n²+1 to count the frequency of each number in the matrix.

Next, we traverse i∈[1,n²]. 
If cnt[i]=2, then i is the duplicated number, and we set the first element of the answer to i. 
If cnt[i]=0, then i is the missing number, and we set the second element of the answer to i.

The time complexity is O(n²), and the space complexity is O(n²). Here, n is the side length of the matrix.
'''

class Solution:
  def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
      count = [1]+[0]*len(grid)**2      # padding for 1-indexed
      
      for lst in grid:
          for num in lst:
              count[num]+=1
        
    return [count.index(2),count.index(0)]
        












































#Approach:Just for fun, using hashmap
#TC:O(n²)
#SC:O(n²)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = Counter()    #defaultdict(int)
        for r in range(n):
            for c in range(n):
                cnt[grid[r][c]]+=1
                
        for i in range(1,n**2+1):
            if cnt[i]==2:
                rep = i
            elif cnt[i]==0:
                miss = i
                
        return [rep,miss]