#Approach:Fast and Slow Pointer
class Solution:
    def isHappy(self, n: int) -> bool:
        slow , fast = n , n 
        while True:
            slow = self.find_square_sum(slow)  # move one step , observe we are passing variable slow in function
            fast = self.find_square_sum(self.find_square_sum(fast)) #move two steps, observe we are passing variable fast in inner function

            if slow == fast: # found the cycle
                break
        return slow ==1 # see if the cycle is stuck on the number '1'

    def find_square_sum(num):
        sq_sum = 0 #define the operation variable
        while num>0:
            r = num % 10
            sq_sum += r*r #operation
            num = num//10
        return sq_sum



#Approach: Using set and Recursion

class Solution:
    def isHappy(self, n: int) -> bool:

        def happyNumber(num):
            seen_number = set()

            while num!=1 and num not in seen_number:
                seen_number.add(num)
                num = sum(int(digit)**2 for digit in str(num))
            return num==1

        return happyNumber(n)

