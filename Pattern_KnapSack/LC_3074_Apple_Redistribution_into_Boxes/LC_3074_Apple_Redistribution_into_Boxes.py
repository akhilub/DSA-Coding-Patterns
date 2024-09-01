#Approach: Greedy + Sorting

'''
This is a type of the Knapsack Problems. 
To formulize the given problem as a Knapsack problem, we need to adapt it to the classic knapsack model.
The standard knapsack problem typically involves selecting items with given weights to maximize the total weight without exceeding the capacity of the knapsack. 
However, the given problem involves distributing apple packs into boxes with certain capacities, and we need to minimize the number of boxes used.

We can solve this by greedily selecting a larger box to fill the items/apples.
As we can unpack the packs of apples, so the only thing matters is the total number of the items:

Then, we start by sorting the capacity array in descending order. This helps to try and fill the boxes with the largest capacity first, potentially minimizing the number of boxes needed.

Then, we use a greedy approach to select the minimum number of boxes. Iterate through the sorted capacities and keep adding boxes until the sum of the capacities is at least total_apples. 
Alternatively, we can iterate over the boxes from larger to smaller capacity, and then deduct the apples until we have filled the boxes with the items.

The time complexity of this solution is O(N+MLogM).
'''

class Soluton:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        #O(N)
        T_apples = sum(apple)
        if T_apples>sum(capacity):
            return -1
       
        #O(MlogM)
        C = sorted(capacity,reverse=True)
        i = 0
        
        ##O(M)
        while T_apples:
            if T_apples>C[i]:
                T_apples-=C[i]
                i+=1
            else:#apples are 0 or -ve
                break
        return i+1
