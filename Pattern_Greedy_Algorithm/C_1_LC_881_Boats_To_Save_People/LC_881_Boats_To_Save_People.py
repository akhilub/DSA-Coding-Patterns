#Approach : Greedy , Two Pointer + Sorting

#1)Sort the people weight array
#2)Intialize two pointer : Set two pointers l at the start lightest ans r at the end heaviest
#3)Select Optimal Pairs: Iterate through the array and pair the lighest person with the heaviest person if their comnbined weight is within the limit
#4)Count Boats: For each iteration , incremenet the boat count .Move the r pointer towards the left 
#5)Repeat Unit All are Accounted For:Count until all people are accounted for i.e until l <r
#6) If i ==j increment the boat count by 1 to arrange for the last remaing person

class Solution:
    def numRescueBoats(self,people):
        people.sort()
        l , r = 0 , len(people) - 1 
        ans = 0
        while l < r :
            if people[l] + people [ r] < = limit:
                l+=1
                r-=1
            
            r-=1
            ans+=1

            if l == r:
                ans+=1

            return ans