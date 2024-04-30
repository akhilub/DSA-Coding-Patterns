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