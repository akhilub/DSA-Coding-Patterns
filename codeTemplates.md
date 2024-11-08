## Two pointers: one input, opposite ends
    def fn(arr):
        left = ans = 0
        right = len(arr) - 1

        while left < right:
            # do some logic here with left and right
            if CONDITION:
                left += 1
            else:
                right -= 1
        
        return ans


## Two pointers: two inputs, exhaust both
    def fn(arr1,arr2):
        i = j= ans =0
        while i< len(arr1) and j < len(arr2):
            #do some logic
            if CONDITION:
                i+=1
            else:
                j+=1
        
        while i< len(arr1):
            #do logic
            i+=1
        
        while j< len(arr2):
            #do logic
            j+=1
        
        return ans

## Find number of subarrays that fit an exact criteria
    from collections import defaultdict

    def fn(arr, k):
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in arr:
            # do logic to change curr
            ans += counts[curr - k]
            counts[curr] += 1
        
        return ans


## Sliding window
    def fn(arr):
        left =ans =curr =0

        for right in range(len(arr)):
            #do logic here to add arr[right] to curr

            while WINDOW_CONDITION_BROKEN:
                #remove arr[left] from curr
                left+=1

            # update ans
        return ans

## Sliding_window_fixed

    def sliding_window_fixed(input, window_size):

        ans = window = input[0:window_size]

        for right in range(window_size, len(input)):
            left = right - window_size

            remove input[left] from window
            append input[right] to window

            ans = optimal(ans, window)

        return ans


## Sliding_window_flexible_longest
    def sliding_window_flexible_longest(input):

        initialize window, ans
        left = 0

        for right in range(len(input)):
            append input[right] to window

            while invalid(window):        # update left until window is valid again
                remove input[left] from window
                left += 1

            ans = max(ans, window)        # window is guaranteed to be valid here
        return ans

## Sliding_window_flexible_shortest
    def sliding_window_flexible_shortest(input):

        initialize window, ans
        left = 0

        for right in range(len(input)):
            append input[right] to window
            
            while valid(window):
                ans = min(ans, window)      # window is guaranteed to be valid here
                remove input[left] from window
                left += 1

        return ans






## Backtrack 
    def backtrack(curr, OTHER_ARGUMENTS...):
        if (BASE_CASE):
            # modify the answer
            return
        
        ans = 0
        for (ITERATE_OVER_INPUT):
            # modify the current state
            ans += backtrack(curr, OTHER_ARGUMENTS...)
            # undo the modification of the current state
        
        return ans

## Backtracking

    ans = []
    def dfs(start_index, path, [...additional states]):
        if is_leaf(start_index):
            ans.append(path[:]) # add a copy of the path to the result
            return
        for edge in get_edges(start_index, [...additional states]):
            # prune if needed
            if not is_valid(edge):
                continue
            path.add(edge)
            if additional states:
                update(...additional states)
            dfs(start_index + len(edge), path, [...additional states])
            # revert(...additional states) if necessary e.g. permutations
            path.pop()


# Build a prefix sum
    def fn(arr):
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] + arr[i])
        
        return prefix


# Binary Search
    def fn(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:  # found the target
                # do something
                return
            if arr[mid] > target:
            #update right pointer because target lies in left half
                right = mid - 1
            else:
            #update left pointer because target lies in right half
                left = mid + 1
        
        # left is the insertion point
        return left


# Binary search: for greedy problems
## Case: Problem Function  is monotonically decreasing 
- If looking for a minimum   

    def fn(arr):
        def check(x):
            # this function is implemented depending on the problem
            return BOOLEAN

        left = MINIMUM_POSSIBLE_ANSWER
        right = MAXIMUM_POSSIBLE_ANSWER
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left


## Case: Problem Function  is monotonically increasing
- Just do opposite if looking for maximum
```
    def fn(arr):
        def check(x):
            # this function is implemented depending on the problem
            return BOOLEAN

        left = MINIMUM_POSSIBLE_ANSWER
        right = MAXIMUM_POSSIBLE_ANSWER
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
    return right
```


## Binary search: duplicate elements, left-most insertion point
- bisect.bisect_left(arr:List[int],target:int) implementation

```
    def fn(arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
```


## Binary search: duplicate elements, right-most insertion point

    def fn(arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid
            else:
                left = mid + 1

        return right



**Note for Binary Search Genric Template:**
- PROBLEM_CONDITION => F() COMPARISON_OPERATOR target   
- On LHS `F()` could be `arr;f();LLinkedList`  
- On RHS `target` would be `some value` to compare





**Note**
```
For the graph templates, assume the nodes are numbered from 0 to n - 1 and the graph is given as an adjacency list. Depending on the problem, you may need to convert the input into an equivalent adjacency list before using the templates.
```

## Graph: BFS

    from collections import deque

    def fn(graph: dict):
        queue = deque([START_NODE])
        seen = {START_NODE}                 # or seen = set([START_NODE])
        ans = 0

        while queue:
            node = queue.popleft()
            # do some logic
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        return ans




## Graph: DFS (iterative)

    def fn(graph: dict):
        stack = [START_NODE]
        seen = {START_NODE}
        ans = 0

        while stack:
            node = stack.pop()
            # do some logic
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        return ans



## Graph: DFS (recursive)

    def fn(graph: dict):
        def dfs(node):
            ans = 0
            # do some logic
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            
            return ans

        seen = {START_NODE}
        return dfs(START_NODE)







## Common model of monotonic stack: 

### Find the nearest number to the left/right of each number that is larger/smaller than it. 

#### Template:

```
stk = []
for i in range(n):
    while stk and check(stk[-1], i):
        stk.pop()
    stk.append(i)
```


### Template - mono_stack

    def mono_stack(insert_entries):
        stack = []
        for entry in insert_entries:
            while stack and stack[-1] <= entry:
                stack.pop()
                # Do something with the popped item here
            stack.append(entry)



### Monotonic increasing stack
 
- The same logic can be applied to maintain a monotonic queue.

```
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)
    
    return ans
```

### Find top k elements with heap

    import heapq

    def fn(arr, k):
        heap = []
        for num in arr:
            # do some logic to push onto heap according to problem's criteria
            heapq.heappush(heap, (CRITERIA, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for num in heap]


### Find number of subarrays that fit an exact criteria

    from collections import defaultdict

    def fn(arr, k):
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in arr:
            # do logic to change curr
            ans += counts[curr - k]
            counts[curr] += 1
        
        return ans