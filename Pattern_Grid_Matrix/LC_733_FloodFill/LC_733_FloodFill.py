#Approach1 ---> Standard DFS
# We will start from the input/given starting cell
# Perform the DFS/BFS to explore the connected cells of same color
# DFS 
    # Check for boundaries return if you go out
    # Check for the cell color return if not intial Color meaning cell is not connected (has been visited or any other color)
    # update the cell with newColor
    # Explore all the neighbor

#Application : Editing Tools Software
class Solution:
    def floodFill(self,image,sr,sc,color):
        if image[sr][sc]==color:
            return image
        rows = len(image)
        cols = len(image[0])
        def dfs(image,r,c,intialColor,newColor):
            if r<0 or r>=rows or c<0 or c>=cols: #out of bound
                return 
            
            if image[sr][sc] != initalColor:  # return if not the required color
                return 

            image[r][c]=newColor
            dfs(image,r-1,c,intialColor,newColor)
            dfs(image,r+1,c,intialColor,newColor)
            dfs(image,r,c-1,intialColor,newColor)
            dfs(image,r,c+1,intialColor,newColor)
            return
            
        dfs(image,sr,sc,image[sr][sc],color)
        return image




#We can perform the flood fill in Recursive DFS Algorithm which is easy
#to implement but at the risk of a stack overflow especially if the field to fill is large

#Alternatively we can implement this using iterative apporach in the fashion of either DFS or BFS
#We can follow the four directions as long as the neighbour pixels are of same color as the starting pixel


#Approach 2  
#RECURSIVE DFS FLOOD FILL 
#Start filling the pixel as long as they have not been seen and also are the same color with the start pixel
#This recursive dfs is fine in small image but tend to cause stack overflow in practical use
class Solution:
    def floodFill(self,image,sr,sc,newColor):
        R,C = len(image), len(image[0])
        
        initialColor = image[sr][sc]
        seen =set()
        def dfs(r,c):
            if (r,c) in seen:
                return 
            seen.add((r,c))
            image[r][c] = newColor
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<R and 0<=nc<C:
                    if image[nr][nc]==initialColor:
                        dfs(nr,nc)
        dfs(sr,sc)
        return image



#Approach 3
#ITERATIVE BFS/DFS FLOOD FILL

#We will use a queue to implement the BFS algo to flood fill the image
class Solution:
    def floodFill(self,image,sr,sc,newColor):
        R,C =len(image), len(image[0])
        Q = deque([(sr,sc)])
        initalColor = image[sr][sc]
        seen = set()
        while Q:
            r,c = Q.popleft()
            image[r][c] = newColor
            if (r,c) in seen:
                continue   # meaning if (r,c) is in notebook skip that loop
            seen.add(r,c)
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<R and 0<nc<C:
                    if image[nr][nc]==initalColor: # we only fill the neighbour if the its the same inital color
                        Q.append((nr,nc))
        return image


#(Using Stack)
#By replacing the queue with stack - this is similar to Recursion
class Solution:
    def floodFill(self,image,sr,sc,newColor):
        R,C = len(image), len(image[0])
        initalColor = image[sr][sc]
        stack = [(sr,sc)]
        seen = set()
        while stack:
            r,c = stack.pop(0)
            image[r][c]=newColor
            seen.add((r,c))

            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<R and 0<=nc<C:
                    if image[nr][nc]==initalColor:
                        stack.append((nr,nc))
        return image

