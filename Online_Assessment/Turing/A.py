def solution(cards):
    # Map to store sum of duplicate card values
    points_map = {}
    for card in cards:
        points_map[card] = points_map.get(card, 0) + card
        
    dp = {}
    def dfs(val):
        # Base case: beyond max card value
        if val > max(points_map.keys()):
            return 0
        # Return memoized result if exists    
        if val in dp:
            return dp[val]
        curr = points_map.get(val, 0)
        # Try taking current value + values 3+ steps away OR skip current value
        dp[val] = max(curr + max((dfs(val+3), dfs(val+4), dfs(val+5)), default=0), 
                      max((dfs(val+1), dfs(val+2)), default=0))
        return dp[val]
        
    return dfs(min(points_map.keys()))







def solution(cards):
    # Create points map
    points_map = {}
    for card in cards:
        points_map[card] = points_map.get(card, 0) + card
    
    # Sort unique values
    values = sorted(points_map.keys())
    n = len(values)
    dp = [0] * n
    
    # Base case
    dp[0] = points_map[values[0]]
    if n == 1:
        return dp[0]
    
    # Fill dp array
    for i in range(n):
        curr_points = points_map[values[i]]
        valid_prev = 0
        
        # Find last valid value we can combine with
        for j in range(i-1, -1, -1):
            if values[i] - values[j] > 2:
                valid_prev = dp[j]
                break
                
        dp[i] = max(dp[i-1], valid_prev + curr_points)
    
    return dp[n-1]
