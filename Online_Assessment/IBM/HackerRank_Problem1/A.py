#TC:O(n+m)
#SC:O(m)
def groupDivision(levels, maxSpread):
    max_level = max(levels)
    count = [0] * (max_level + 1)
    
    for level in levels:
        count[level] += 1
    
    groups = 0
    start = 0
    
    for level in range(1, max_level + 1):
        if count[level] > 0:
            if start == 0:
                start = level
                groups += 1
            elif level - start > maxSpread:
                start = level
                groups += 1
    
    return groups


#TC:O(nlogn)
#SC:O(n)

def groupDivision(levels, maxSpread):
    levels = sortes(levels)  # Sort the levels in ascending order
    groups = 1
    start = levels[0]
    
    for level in levels[1:]:
        if level - start > maxSpread:
            groups += 1
            start = level
    
    return groups