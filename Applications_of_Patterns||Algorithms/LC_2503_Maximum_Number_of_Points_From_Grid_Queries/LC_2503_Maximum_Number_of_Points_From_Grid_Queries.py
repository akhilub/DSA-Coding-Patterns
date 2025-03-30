#Approach : BFS +PQ (MinHeap)
#When input modification is allowed



class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m , n = len(grid) , len(grid[0])
        ans = [0]*len(queries)
        cnt = 0
        pq = [(grid[0][0],0,0)]   # (grid[i][j], i, j)
        grid[0][0] = 'v'          # or grid[0][0] = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        qs = sorted(enumerate(queries), key = lambda x:x[1])  #sorting queries based on values [...,(ind,val),...]
        
        for qi,qv in qs:
            while pq and pq[0][0]<qv:
                val, i , j = heappop(pq)
                cnt+=1
                for di,dj in directions:
                    ni , nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n:
                        if grid[ni][nj]!='v':  #if grid[ni][nc]:  or if grid[ni][nc]!=0: 
                            heappush(pq,(grid[ni][nj],ni,nj))
                            grid[ni][nj] = 'v'
            ans[qi] = cnt

        return ans


#qs = sorted((v, i) for i, v in enumerate(queries))   # sorting queries based on values [...,(val,ind),...]
#qs = sorted(enumerate(queries), key = lambda x:x[1]) # sorting queries based on values [...,(ind,val),...]
#qs = sorted(enumerate(queries))                      # sorting queries bases on indexes[...,(ind,val),...]









#Approach : BFS +PQ (MinHeap)
#When input modification is not allowed

'''
According to the problem description, each query is independent, the order of the queries does not affect the result, and we are required to start from the top left corner each time, counting the number of cells that can be accessed and whose value is less than the current query value.
Therefore, we can first sort the queries array, and then process each query in ascending order.
We use a priority queue (min heap) to maintain the smallest cell value that we have currently accessed, and use an array or hash table vis to record whether the current cell has been visited. Initially, we add the data (grid (0][0], 0, 0) of the top left cell as a tuple to the priority queue, and set vis[0][0] to True.
For each query queries[i], we judge whether the minimum value of the current priority queue is less than queries[i]. If it is, we pop the current minimum value, increment the counter cnt, and add the four cells above, below, left, and right of the current cell to the priority queue, noting to check whether they have been visited. Repeat the above operation until the minimum value of the current priority queue is greater than or equal to queries[i], at which point cnt is the answer to the current query.
The time complexity is O(k x logk + m x n log(m X n)), and the space complexity is O(m X n). Where m and n are the number of rows and columns of the grid, and k is the number of queries. We need to sort the queries array, which has a time complexity of O(k x log k). Each cell in the matrix will be visited at most once, and the time complexity of each enqueue and dequeue operation is O(log(m X n)). Therefore, the total time complexity is O(k x log k + m x n log(m x n).

'''




class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m , n = len(grid), len(grid[0])
        ans = [0]*len(queries)
        cnt = 0
        pq = [(grid[0][0],0,0)]
        vis = set()          #vis = [[False]*n for _ in range(m)]
        vis.add((0,0))       #vis[0][0] = True
        cnt = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        qs = sorted((v,i) for i,v  in enumerate(queries))

        for qv,qi in qs:
            while pq and pq[0][0]<qv:
                _ , i ,j = heappop(pq)
                cnt+=1
                for di,dj in directions:
                    ni , nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n:
                        if (ni,nj) not in vis:                  #if not vis[ni][nj]:  #meaning vis[ni][nj] is True
                            heappush(pq,(grid[ni][nj],ni,nj))
                            vis.add((ni,nj))                    #vis[ni][nj] = True

            ans[qi] = cnt
        return ans



'''
vis = set()
vis.add((0,0))
    ||
    ||
    ||
vis = {(0,0)}
'''
