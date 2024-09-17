from math import ceil

def distribute_parcels(parcels, extra_parcels):
    #left, right = max(parcels), max(max(parcels), sum(parcels) + extra_parcels) // len(parcels)
    
    # left, right = max(parcels), (sum(parcels) + extra_parcels) // len(parcels)
    
    # left, right = max(parcels), (sum(parcels) + extra_parcels)
    
    # left, right = max(parcels), (sum(parcels) + extra_parcels + len(parcels) - 1) // len(parcels)
    
    
    left, right = max(parcels), max(parcels)+extra_parcels
    
    
    # left, right = min(parcels), (sum(parcels) + extra_parcels) // len(parcels)
    
    print(left,right)
    
    while left < right:
        print(left,right)
        mid = (left + right) // 2
        
        needed = sum(max(0, mid - p) for p in parcels)
    
        if needed <= extra_parcels:
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage
parcels = [7, 5, 1, 9, 11]
extra_parcels = 25

result = distribute_parcels(parcels, extra_parcels)
print(f"The minimum possible maximum number of parcels any agent must deliver: {result}")

# Calculate final distribution
final_distribution = parcels.copy()
for i in range(len(parcels)):
    if extra_parcels > 0:
        add = min(result - parcels[i], extra_parcels)
        final_distribution[i] += add
        extra_parcels -= add

print("\nAn optimal assignment is shown.")
print("\nParcels\tExtra Parcels\tTotal Parcels")
for original, final in zip(parcels, final_distribution):
    extra = final - original
    print(f"{original}\t{extra}\t\t{final}")









parcels = [2, 2] 
extra_parcels = 10

result = distribute_parcels(parcels, extra_parcels)
print(f"The minimum possible maximum number of parcels any agent must deliver: {result}")


# Calculate final distribution
final_distribution = parcels.copy()
for i in range(len(parcels)):
    if extra_parcels > 0:
        add = min(result - parcels[i], extra_parcels)
        final_distribution[i] += add
        extra_parcels -= add

print("\nAn optimal assignment is shown.")
print("\nParcels\tExtra Parcels\tTotal Parcels")
for original, final in zip(parcels, final_distribution):
    extra = final - original
    print(f"{original}\t{extra}\t\t{final}")
