#[[2,7],[4,5]]
#{0:1,1:2,2,:4}

def pairsSum(nums,target):
    n = len(nums)
    seen = {}
    ans = []
    for i in range(n):
        diff = target - nums[i]
        if diff in seen:
            ans.append([diff,nums[i]])
        seen[nums[i]]=nums[i]
    return ans


def validate_inputs():
    # Test Case 1: Valid Input
    try:
        nums1 = [1, 2, 4, 7, 5]
        target1 = 9
        for num in nums1:
            if not isinstance(num, int):
                raise TypeError("Array must contain only integers")
        print("Valid Test Case:")
        print(f"Input: {nums1}")
        print(f"Result: {pairsSum(nums1, target1)}\n")
        
    except TypeError as e:
        print(f"Error: {e}\n")

    # Test Case 2: Invalid Input
    try:
        nums2 = [1, 2, 'a', 7, 5]
        target2 = 9
        for num in nums2:
            if not isinstance(num, int):
                raise TypeError("Array must contain only integers")
        print(pairsSum(nums2, target2))
        
    except TypeError as e:
        print("Invalid Test Case:")
        print(f"Input: {nums2}")
        print("Error caught: Array contains non-integer values\n")

# Run the validation tests
validate_inputs()