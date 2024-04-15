
#Competative Programming approach
#We will initialize two pointer left and right at the start and end of the window of size k
#Then we will take the curr_sum of the subarray in the window of size k
#Later we are going to traverse the window by sliding and compare the curr_sum of the current and previous subarray/window and store it into the max_sum 

class Solution:
    def max_subarray_of_size_k(self,k,arr):
        max_sum = 0
        curr_sum =0
        n = len(arr)
        for i in range(n-k+1):
            left = i
            right = i+k
            curr_sum = sum(arr[left:right])
            max_sum = max(max_sum,curr_sum)

        return max_sum

if __name__ == "__main__":
    sol =Solution()
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 =3
    res1 = sol.max_subarray_of_size_k(k1,arr1)
    print("maximum sum of subarray of size K is ", res1)

    arr2 = [2, 3, 4, 1, 5]
    k2 =2
    res2 = sol.max_subarray_of_size_k(k2,arr2)
    print("maximum sum of subarray of size K is ", res2)


#Sliding Window Expanded Approach
#TC:O(n)
#SC:O(1)

class Solution:
    def max_subarray_of_size_k(self,k,arr):
        max_sum = 0
        win_start = 0
        n = len(arr)
        win_sum =0     
        for win_end in range(n):
            win_sum+=arr[win_end] # add the element of subarray
            #slide the window, no need to slide if we have not reached the required window size of k
            if win_end>=k-1:
                max_sum = max(max_sum,win_sum)
                win_sum-=arr[win_start] #subtract the outgoing element from win_sum
                win_start+=1 # slide the window ahead

        return max_sum

if __name__ == "__main__":
    sol =Solution()
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 =3
    res1 = sol.max_subarray_of_size_k(k1,arr1)
    print("maximum sum of subarray of size K is ", res1)

    arr2 = [2, 3, 4, 1, 5]
    k2 =2
    res2 = sol.max_subarray_of_size_k(k2,arr2)
    print("maximum sum of subarray of size K is ", res2)