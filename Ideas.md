## Convert Graph Adjacency Matrix input to Adjacency List output

<table>

<tr>
<th>Way 1</th>
<th>Way 2</th>
</tr>

<tr>
<td>
<pre>
def adj_list(grid):
    G={}
    for i in range(len(grid)):
        neighbors = []
        for j in range(len(grid[i])):
            if grid[i][j]==1 and i!=j: #Exclude self loop           
                neighbors.append(j)
        G[i] = neighbors
    return G

grid = [[1,1,0],[1,1,0],[0,0,1]] //adjacency matrix
G = adj_list(grid)

print(G) //G is now {0: [1], 1: [0], 2: []}
</pre>
</td>


<td>
<pre>
def adj_list(grid):
    G=defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1 and i!=j: #Exclude self loop           
                G[i].append(j)
    return G

grid = [[1,1,0],[1,1,0],[0,0,1]] //adjacency matrix
G = adj_list(grid)

print(G) // G is now defaultdict(<class 'list'>, {0: [1], 1: [0]})
</pre>
</td>


</tr>
</table>
