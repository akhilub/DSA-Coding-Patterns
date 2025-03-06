from collections import Counter 

def mostFrequentElement(nums):
    cnt = Counter(nums)
    sorted_dict = sorted(cnt.items(), key= lambda x:x[1])
    return sorted_dict[0][1]


nums = [1,1,1,2,3,2]
print(mostFrequentElement(nums))