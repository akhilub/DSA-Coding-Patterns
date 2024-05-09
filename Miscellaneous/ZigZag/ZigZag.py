#Long Approach 
# - Your Logic is absolutely correct
# - will Cost you time
# - start using python inbuilt functions & libraries
# - This could be done in very short way using python data structures

# def solution(numbers):     
    # def zigzag(arr):
    #     if arr[0]<arr[1] and arr[1]>arr[2]:
    #         return 1
    #     elif arr[0]>arr[1] and arr[1]<arr[2]:
    #         return 1
    #     return 0
    
    # res = []
    # for i in range(len(numbers)-2):
    #     l = i
    #     r = i+2
    #     arr = numbers[l:r+1]
    #     res.append(zigzag(arr))
    #     print(res)
    # return res

#Approach 2
def solution(numbers):
    zigzag = [0]*(len(numbers)-2)
    for i in range(len(numbers)-2):
        if numbers[i]<numbers[i+1]>numbers[i+2] or numbers[i]>numbers[i+1]<numbers[i+2]:
            zigzag[i]=1
    return zigzag


if __name__ =="__main__":
    numbers = [1, 2, 1, 3, 4]
    result = solution(numbers)
    print(result)  # Output: [1, 1, 0]

    numbers = [1, 2, 3, 4]
    result = solution(numbers)
    print(result)  # Output: [0, 0]

    numbers = [1000000000, 1000000000, 1000000000]
    result = solution(numbers)
    print(result)  # Output: [0]
