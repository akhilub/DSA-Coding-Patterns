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



## Sliding_window_fixed

    def sliding_window_fixed(input, window_size):

        ans = window = input[0:window_size]

        for right in range(window_size, len(input)):
            left = right - window_size

            remove input[left] from window
            append input[right] to window

            ans = optimal(ans, window)

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


- Just do opposite if looking for maximum

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



# Build a prefix sum
    def fn(arr):
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] + arr[i])
        
        return prefix

